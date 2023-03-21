from qiime2.plugin import Plugin
from qiime2.plugin import (Str, Plugin, Choices, List, Citations, Range, Int,
                           Float, Visualization, Bool, TypeMap, Metadata,
                           MetadataColumn, Categorical)
from q2_types.feature_table import FeatureTable, Frequency
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
    inputs={'a': FeatureTable[Frequency], 'b': FeatureTable[Frequency]},
    parameters={},
    outputs=[('shared_asvs', FeatureTable[Frequency])],
    input_descriptions={
        'a': 'Feature table artifact for the first sample',
        'b': 'Feature table artifact for the second sample'
    },
    parameter_descriptions={},
    output_descriptions={
        'shared_asvs': 'Feature table artifact with shared ASVs between the two samples'
    },
    name='Compute generates FeatureTable data',
    description='Computes the shared ASVs between two feature tables using Qiime2.'
)
