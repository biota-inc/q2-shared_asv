import qiime2
import pandas as pd
from qiime2.plugin import Plugin
from q2_feature_table import filter_features, filter_samples
from q2_types.feature_table import (
    FeatureTable, Frequency, RelativeFrequency, PresenceAbsence, Composition)
import biom

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

    # Compute the shared ASVs
    shared_asvs = filter_features(
        table=filtered_table,
        min_frequency=percentage,
        min_samples=2,
    )

    return shared_asvs