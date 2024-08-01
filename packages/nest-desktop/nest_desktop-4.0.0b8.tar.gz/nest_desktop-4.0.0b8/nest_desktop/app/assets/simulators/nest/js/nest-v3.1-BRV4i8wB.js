const e=`{{ #simulation.code.importModules }}
import nest
import numpy as np
{{ /simulation.code.importModules }}
{{ #simulation.code.resetKernel }}

nest.ResetKernel()
{{ /simulation.code.resetKernel }}
{{ #simulation.code.runSimulationInsite }}

try:
  nest.Install('insitemodule')
except:
  pass
{{ /simulation.code.runSimulationInsite }}
{{ #simulation.code.setKernelStatus }}

# Set simulation kernel
nest.SetKernelStatus({
  "local_num_threads": {{ simulation.kernel.localNumThreads }},
  "resolution": {{ simulation.kernel.resolution }},
  "rng_seed": {{ simulation.kernel.rngSeed }}
})
{{ /simulation.code.setKernelStatus }}
{{ #simulation.code.createNodes }}
{{ #network.hasNodeModels }}

# Copy node models
{{ #network.modelsCopied.nodeModels }}
nest.CopyModel("{{ existingModelId }}", "{{ newModelId }}"{{ #hasSomeVisibleParams }}, params={
{{ #filteredParams }}
  "{{ id }}": {{ &valueAsString }},
{{ /filteredParams }}
}{{ /hasSomeVisibleParams }})
{{ /network.modelsCopied.nodeModels }}
{{ /network.hasNodeModels }}

# Create nodes
{{ #network.nodes }}
{{ view.label }} = nest.Create("{{ modelId }}"{{ #sizeVisible }}, {{ n }}{{ /sizeVisible }}{{ #hasSomeVisibleParams }}, params={
{{ #filteredParams }}
  "{{ id }}": {{ &valueAsString }},
{{ /filteredParams }}
{{ #model.isRecorder }}
{{ #model.isMultimeter }}
  "record_from": {{ &recordsFixed }},
{{ /model.isMultimeter }}
{{ #simulation.code.runSimulationInsite }}
  "record_to": "insite",
{{ /simulation.code.runSimulationInsite }}
{{ /model.isRecorder }}
}{{ /hasSomeVisibleParams }}{{ #spatial.positions }}, positions={{ &spatial.code }}{{ /spatial.positions }})
{{ /network.nodes }}
{{ /simulation.code.createNodes }}
{{ #simulation.code.connectNodes }}
{{ #network.modelsCopied.hasSynapseModels }}

# Copy synapse models
{{ #network.modelsCopied.synapseModels }}
nest.CopyModel("{{ existingModelId }}", "{{ newModelId }}"{{ #hasSomeVisibleParams }}, params={
{{ #filteredParams }}
  "{{ id }}": {{ &valueAsString }},
{{ /filteredParams }}
}{{ /hasSomeVisibleParams }})
{{ /network.modelsCopied.synapseModels }}
{{ /network.modelsCopied.hasSynapseModels }}

# Connect nodes
{{ #network.connections }}
nest.Connect({{ source.view.label }}{{ sourceSlice.indices }}, {{ target.view.label }}{{ targetSlice.indices }}{{ #hasConnSpec }}{{ ^hasSomeVisibleParams }}, "{{ rule.value }}"{{ /hasSomeVisibleParams }}{{ #hasSomeVisibleParams }}, conn_spec={
  "rule": "{{ rule.value }}",
{{ #filteredParams }}
  "{{ id }}": {{ code }},
{{ /filteredParams }}
}{{ /hasSomeVisibleParams }}{{ /hasConnSpec }}{{ #synapse.hasSynSpec }}, syn_spec={{ ^synapse.hasSomeVisibleParams }}"{{ synapse.modelId }}"{{ /synapse.hasSomeVisibleParams }}{{ #synapse.hasSomeVisibleParams }}{ {{ ^synapse.isStatic }}
  "synapse_model": "{{ synapse.modelId }}",{{ /synapse.isStatic }}
{{ #synapse.filteredParams }}
  "{{ id }}": {{ code }},
{{ /synapse.filteredParams }}
}{{ /synapse.hasSomeVisibleParams }}{{ /synapse.hasSynSpec }})
{{ /network.connections }}
{{ /simulation.code.connectNodes }}

{{ #simulation.code.prepareSimulation }}
# Prepare simulation
nest.Prepare()
{{ /simulation.code.prepareSimulation }}
{{ #simulation.code.runSimulation }}
# Run simulation
nest.Simulate({{ simulation.time }})

{{ ^simulation.code.runSimulationInsite }}
{{ #network.someSpatialNodes }}
# Get positions
def getPositions(nodes):
    positions = {}
    for node in nodes:
        position = nest.GetPosition(node)
        for idx in range(len(node)):
            positions[node[idx].global_id] = position[idx]
    return positions

{{ /network.someSpatialNodes }}
response = {
  "events": [{{ #network.recorders }}{{ view.label }}.events, {{ /network.recorders }}]{{ #network.someSpatialNodes }},
  "positions": getPositions([{{ #network.spatial }}{{ view.label }},{{ /network.spatial }}]){{ /network.someSpatialNodes }}
}
{{ /simulation.code.runSimulationInsite }}
{{ /simulation.code.runSimulation }}
`;export{e as default};
