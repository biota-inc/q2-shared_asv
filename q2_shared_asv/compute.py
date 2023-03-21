import qiime2
import pandas as pd
from qiime2.plugin import Plugin
from q2_feature_table import filter_features
from q2_types.feature_table import (
    FeatureTable, Frequency, RelativeFrequency, PresenceAbsence, Composition)

# Define the plugin
plugin = Plugin(
    name='shared-asv',
    version='0.1.0',
    website='https://github.com/biota-inc/q2-shared_asv',
    package='q2_shared_asv',
    description='A QIIME 2 plugin for shared ASV analysis',
    short_description='Plugin for computing shared ASV.',
)

def compute(table: FeatureTable[RelativeFrequency], sample_a: str, sample_b: str, metadata: qiime2.Metadata, percentage: float) -> (FeatureTable[RelativeFrequency]):
    # Filter the feature table to only include sample A and sample B
    filtered_table = qiime2.plugins.feature_table.actions.filter_samples(
        table=table,
        metadata=metadata,
        where=f"sample-id IN ('{sample_a}', '{sample_b}')",
    ).filtered_table

    # Get the ASV frequencies for sample A and sample B
    table_a = filtered_table[[sample_a]]
    table_b = filtered_table[[sample_b]]

    # Merge the tables
    merged_table = table_a.merge(table_b, how='inner', left_index=True, right_index=True)

    # Get the total relative frequency for each ASV across the two samples
    table_summary = merged_table.sum(axis=1)

    # Filter for ASVs that exceed the specified threshold of relative frequency
    shared_asvs_table = table_summary[table_summary > percentage]

    # Create an artifact from the shared_asvs_table
    shared_asvs_artifact = qiime2.Artifact.import_data('FeatureTable[RelativeFrequency]', shared_asvs_table)

    return shared_asvs_artifact