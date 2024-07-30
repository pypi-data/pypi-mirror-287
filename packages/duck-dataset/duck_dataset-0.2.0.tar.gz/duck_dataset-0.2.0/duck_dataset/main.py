from pathlib import Path
from functools import partial

from pydantic import BaseModel, field_validator, Field
import duckdb
from . import aggregations


class DuckDataset(BaseModel):
    path: str = './dataset.duckdb'

    @field_validator('path')
    def check_path(cls, v: str):
        v = Path(v)
        if not v.exists():
            raise ValueError(f'Path {v} does not exist')
        return v
    
    @property
    def db_path(self):
        return str(Path(self.path).resolve())
    
    @property
    def layers(self) -> dict:
        with duckdb.connect(self.db_path, read_only=True) as duck:
            return {_id: title for (_id, title) in duck.execute('SELECT id, title FROM metadata;').fetchmany()}
    
    @property
    def aggregations(self):
        with duckdb.connect(self.db_path, read_only=True) as duck:
            return duck.execute('FROM aggregations;').df()
    
    def __getitem__(self, key):
        datasets = self.layers
        
        # find the key
        if key in datasets.keys():
            dataset_id = key
        elif key in datasets.values():
            dataset_id = list(datasets.keys())[list(datasets.values()).index(key)]
        else:
            raise KeyError(f'The key {key} was not found. It is not part of the ids or titles of DuckDataset.layers')
        
        # instatiate a new DuckAggregation object
        return DuckAggregation(database=self, dataset_id=dataset_id)
    
    def __contains__(self, key):
        datasets = self.layers
        return key in datasets.keys() or key in datasets.values()


class DuckAggregation(BaseModel, extra='allow'):
    database: DuckDataset = Field(repr=False)
    dataset_id: int

    def model_post_init(self, __context) -> None:
        """
        Add the available aggregations as partial functions
        """
        aggs = self.database.aggregations
        my_aggregations = aggs.where(aggs.id == self.dataset_id).dropna(how='all')

        # add each available aggregation as a partial function
        for _, agg in my_aggregations.iterrows():
            if agg.aggregation_scale == 'spatial':
                self.spatial = partial(aggregations.spatial, db_path=self.database.db_path, function_name=agg.function_name)
            elif agg.aggregation_scale == 'temporal':
                self.temporal = partial(aggregations.temporal, db_path=self.database.db_path, function_name=agg.function_name)
            elif agg.aggregation_scale == 'spatiotemporal':
                self.spatiotemporal = partial(aggregations.spatiotemporal, db_path=self.database.db_path, function_name=agg.function_name)


if __name__ == '__main__':
    dataset = DuckDataset()
    print(dataset.layers)
    print(dataset.aggregations)
    print(dataset[1].spatial)
 