import qiime2
from qiime2.plugin import Plugin
from q2_feature_table import filter_features, filter_samples, merge
from q2_types.feature_table import (
    FeatureTable, Frequency, RelativeFrequency, PresenceAbsence, Composition)
import biom
import numpy as np

# Define the plugin
plugin = Plugin(
    name='shared-asv',
    version='0.2.0',
    website='https://github.com/biota-inc/q2-shared_asv',
    package='q2_shared_asv',
    description='A QIIME 2 plugin for shared ASV analysis',
    short_description='Plugin for computing shared ASV.',
)

def compute(table: biom.Table, sample_a: str, sample_b: str, metadata: qiime2.Metadata, percentage: float) -> biom.Table:
    # Filter the feature table to only include sample A and sample B
    filtered_table = filter_samples(
        table=table,
        metadata=metadata,
        where=f'"sample-id" IN (\'{sample_a}\', \'{sample_b}\')',
    )
    
    # Filter features based on the percentage
    filtered_features_sample_a = filter_features(
        table=filtered_table,
        metadata=metadata,
        where=f'"sample-id"=\'{sample_a}\' AND CAST("frequency" AS FLOAT)>={percentage}',
    )
    
    filtered_features_sample_b = filter_features(
        table=filtered_table,
        metadata=metadata,
        where=f'"sample-id"=\'{sample_b}\' AND CAST("frequency" AS FLOAT)>={percentage}',
    )

    # Check if either table is empty
    if filtered_features_sample_a.shape[0] == 0 or filtered_features_sample_b.shape[0] == 0:
        # Either table is empty, print the message in yellow
        print(f'\033[33mThere is no shared ASVs between {sample_a} and {sample_b}\033[0m')
        return biom.Table(np.zeros((0, 2)), [], [sample_a, sample_b])

    # Merge the filtered feature tables of sample A and sample B
    shared_asvs, _ = merge(
        tables=[filtered_features_sample_a, filtered_features_sample_b],
        overlap_method='sum'
    )
    
    return shared_asvs
