local env = std.extVar("__ksonnet/environments");
local params = std.extVar("__ksonnet/params").components.master_is_chief_v1alpha1;

local k = import "k.libsonnet";

local actualImage = "gcr.io/kubeflow-images-staging/tf-operator-test-server:v20180613-e06fc0bb-dirty-5ef291";
local name = params.name;
local namespace = env.namespace;

local podTemplate = {
  spec: {
    containers: [
      {
        name: "tensorflow",
        image: actualImage,
      },
    ],
  },
};

local job = {
  apiVersion: "kubeflow.org/v1alpha1",
  kind: "TFJob",
  metadata: {
    name: name,
    namespace: namespace,
  },
  spec: {
    replicaSpecs: [
      {
        replicas: 1,
        template: podTemplate,
        tfReplicaType: "MASTER",
      },
      {
        replicas: 2,
        template: podTemplate,
        tfReplicaType: "PS",
      },
      {
        replicas: 4,
        template: podTemplate,
        tfReplicaType: "WORKER",
      },
  ],
},
};  // job.

std.prune(k.core.v1.list.new([job]))
