from qiime2.plugin import Plugin
import pandas as pd

from q2_types.feature_table import Frequency

# Define the plugin
plugin = Plugin(
    name='shared-asv',
    version='0.1.0',
    website='https://github.com/biota-inc/q2-shared_asv',
    package='q2_shared_asv',
    description='A QIIME 2 plugin for shared ASV analysis',
    short_description='Plugin for computing shared ASV.',
)

def compute(a: pd.DataFrame, b: pd.DataFrame) -> pd.DataFrame:
    """
    Compute the Shared ASVs between two FeatureTable.
    """
        
    # Merge the tables
    merged_table = a.merge(b)

    # Get the feature table summary
    table_summary = merged_table.sum(axis=0)

    # Filter for ASVs that are present in both tables
    shared_asvs = table_summary[table_summary > 1]

    return shared_asvs
