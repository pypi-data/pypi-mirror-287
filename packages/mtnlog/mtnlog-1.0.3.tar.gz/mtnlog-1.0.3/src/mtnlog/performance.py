"""Performance logger class for logging performance metrics."""

import os
import psutil

import pandas as pd
from nvitop import ResourceMetricCollector, Device


class PerformanceLogger:
    """Performance logger class."""

    def __init__(self, log_dir, log_node):

        os.makedirs(log_dir, exist_ok=True)

        self.log_dir = log_dir
        self.log_node = log_node
        self.df = pd.DataFrame()
        self.tag = None
        self.filepath = None
        self.collector = ResourceMetricCollector(Device.cuda.all()).daemonize(
            on_collect=self.on_collect,
            interval=1.0,
        )
        self.cpu_count = psutil.cpu_count(logical=False)
        self.start_time = None

    def new_res(self):
        """Returns the directory."""

        os.makedirs(f"{self.log_dir}/{self.tag}", exist_ok=True)

        self.filepath = f"{self.log_dir}/{self.tag}/node-{self.log_node}.csv"

    def change_tag(self, tag):
        """Changes the tag."""
        if self.filepath is not None:
            self.stop()
        self.tag = tag
        self.new_res()

    def stop(self):
        """Stops the collector."""
        if not self.df.empty:
            self.df.to_csv(self.filepath, index=False)
        self.df = pd.DataFrame()

    def get_cpu_usage_per_core(self):
        """Returns the CPU usage per core."""
        cpu_percent = psutil.cpu_percent(interval=0.1, percpu=True)
        return {f"cpu_core_{i+1}": percent for i, percent in enumerate(cpu_percent[:self.cpu_count])}

    def clean_column_name(self, col):
        """Cleans the column name."""
        if col.startswith("metrics-daemon/host/"):
            col = col[len("metrics-daemon/host/"):]
        return col

    def on_collect(self, metrics):
        """Collects metrics."""

        metrics['tag'] = self.tag

        cpu_metrics = self.get_cpu_usage_per_core()
        metrics.update(cpu_metrics)

        df_metrics = pd.DataFrame.from_records([metrics])

        df_metrics.columns = [self.clean_column_name(col) for col in df_metrics.columns]

        if self.df.empty:
            self.df = df_metrics
        else:
            for col in df_metrics.columns:
                if col not in self.df.columns:
                    self.df[col] = None

            self.df = pd.concat([self.df, df_metrics], ignore_index=True)

        return True
