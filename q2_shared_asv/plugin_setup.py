from qiime2.plugin import (Str, Plugin, Choices, List, Citations, Range, Int,
                           Float, Visualization, Bool, TypeMap, Metadata,
                           MetadataColumn, Categorical)
from q2_types.feature_table import (
    FeatureTable, Frequency, RelativeFrequency, PresenceAbsence, Composition)
from q2_types.feature_data import FeatureData
from q2_feature_table import filter_features
from q2_shared_asv.compute import compute

plugin = Plugin(
    name='shared-asv',
    version='0.1.0',
    website='https://github.com/biota-inc/q2-shared_asv',
    package='q2_shared_asv',
    description='A QIIME 2 plugin for shared ASV analysis',
    short_description='Plugin for computing shared ASV.',
)

# Register the function as an artifact method
plugin.methods.register_function(
    function=compute,
    inputs={
        'table': FeatureTable[RelativeFrequency],
    },
    parameters={
        'sample_a': Str,
        'sample_b': Str,
        'metadata': Metadata,
        'percentage': Float % Range(0, 1, inclusive_start=True, inclusive_end=True),
    },
    outputs=[
        ('shared_asvs', FeatureTable[RelativeFrequency]),
    ],
     input_descriptions={
        'table': 'The feature table containing the samples for which shared ASVs should be computed.',
    },
    parameter_descriptions={
        'sample_a': 'The first sample for which shared ASVs should be computed.',
        'sample_b': 'The second sample for which shared ASVs should be computed.',
        'metadata': 'The sample metadata for sample-id',
        'percentage': 'The threshold for filtering shared ASVs based on relative frequency.',
    },
    output_descriptions={
        'shared_asvs': 'The resulting feature table containing the shared ASVs between the two samples.',
    },
    name='Compute Shared ASVs',
    description='Compute the Shared ASVs between two samples within a FeatureTable',
)
