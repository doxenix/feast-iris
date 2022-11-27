from datetime import timedelta

from feast import Entity, FeatureService, FeatureView, Field, FileSource, ValueType
from feast.types import Float64, Int64, String

patient = Entity(name = "Id",
                     value_type = ValueType.INT64,
                 description = "ID of flower")

## Predictors Feature View
file_source = FileSource(path = r"data/predictors_df.parquet",
                         event_timestamp_column = "event_timestamp",)

df1_fv = FeatureView(
    name = "predictors_df_feature_view",
    #ttl = timedelta(seconds = 86400*2),
    entities = ['Id'],
    schema = [
    Field(name = "SepalLengthCm", dtype = Float64),
    Field(name = "SepalWidthCm", dtype = Float64),
    Field(name = "PetalLengthCm", dtype = Float64),
    Field(name = "PetalWidthCm", dtype = Float64)      
    ],
    source = file_source,
    online = True,
    tags= {},
)

## Target FEature View

target_source = FileSource(path = r"data/target_df.parquet",
                         event_timestamp_column = "event_timestamp",)

target_fv = FeatureView(
    name = "target_df_feature_view",
    #ttl = timedelta(seconds = 86400*2),
    entities = ['Id'],
    schema = [
    Field(name = "Species", dtype = String),       
    ],
    source = target_source,
    online = True,
    tags= {},
)