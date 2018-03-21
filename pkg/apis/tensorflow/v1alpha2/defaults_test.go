// Copyright 2018 The Kubeflow Authors
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package v1alpha2

import (
	"reflect"
	"testing"

	"k8s.io/api/core/v1"
)

func expectedTFJob() *TFJob {
	return &TFJob{
		Spec: TFJobSpec{
			TFReplicaSpecs: map[TFReplicaType]*TFReplicaSpec{
				TFReplicaTypeWorker: &TFReplicaSpec{
					Replicas:      Int32(1),
					RestartPolicy: RestartPolicyAlways,
					Template: v1.PodTemplateSpec{
						Spec: v1.PodSpec{
							Containers: []v1.Container{
								v1.Container{
									Image: defaultImage,
									Ports: []v1.ContainerPort{
										v1.ContainerPort{
											Name:          defaultPortName,
											ContainerPort: defaultPort,
										},
									},
								},
							},
						},
					},
				},
			},
		},
	}
}

func TestSetDefaultTFJob(t *testing.T) {
	testCases := map[string]struct {
		original *TFJob
		expected *TFJob
	}{
		"set replicas": {
			original: &TFJob{
				Spec: TFJobSpec{
					TFReplicaSpecs: map[TFReplicaType]*TFReplicaSpec{
						TFReplicaTypeWorker: &TFReplicaSpec{
							RestartPolicy: RestartPolicyAlways,
							Template: v1.PodTemplateSpec{
								Spec: v1.PodSpec{
									Containers: []v1.Container{
										v1.Container{
											Image: defaultImage,
											Ports: []v1.ContainerPort{
												v1.ContainerPort{
													Name:          defaultPortName,
													ContainerPort: defaultPort,
												},
											},
										},
									},
								},
							},
						},
					},
				},
			},
			expected: expectedTFJob(),
		},
		"set default image": {
			original: &TFJob{
				Spec: TFJobSpec{
					TFReplicaSpecs: map[TFReplicaType]*TFReplicaSpec{
						TFReplicaTypeWorker: &TFReplicaSpec{
							Replicas:      Int32(1),
							RestartPolicy: RestartPolicyAlways,
							Template: v1.PodTemplateSpec{
								Spec: v1.PodSpec{
									Containers: []v1.Container{
										v1.Container{
											Ports: []v1.ContainerPort{
												v1.ContainerPort{
													Name:          defaultPortName,
													ContainerPort: defaultPort,
												},
											},
										},
									},
								},
							},
						},
					},
				},
			},
			expected: expectedTFJob(),
		},
		"set default port": {
			original: &TFJob{
				Spec: TFJobSpec{
					TFReplicaSpecs: map[TFReplicaType]*TFReplicaSpec{
						TFReplicaTypeWorker: &TFReplicaSpec{
							Replicas:      Int32(1),
							RestartPolicy: RestartPolicyAlways,
							Template: v1.PodTemplateSpec{
								Spec: v1.PodSpec{
									Containers: []v1.Container{
										v1.Container{
											Image: defaultImage,
										},
									},
								},
							},
						},
					},
				},
			},
			expected: expectedTFJob(),
		},
		"set default restart policy": {
			original: &TFJob{
				Spec: TFJobSpec{
					TFReplicaSpecs: map[TFReplicaType]*TFReplicaSpec{
						TFReplicaTypeWorker: &TFReplicaSpec{
							Replicas: Int32(1),
							Template: v1.PodTemplateSpec{
								Spec: v1.PodSpec{
									Containers: []v1.Container{
										v1.Container{
											Image: defaultImage,
											Ports: []v1.ContainerPort{
												v1.ContainerPort{
													Name:          defaultPortName,
													ContainerPort: defaultPort,
												},
											},
										},
									},
								},
							},
						},
					},
				},
			},
			expected: expectedTFJob(),
		},
	}

	for name, tc := range testCases {
		SetDefaults_TFJob(tc.original)
		if !reflect.DeepEqual(tc.original, tc.expected) {
			t.Errorf("%s: Want\n%v; Got\n %v", name, Pformat(tc.expected), Pformat(tc.original))
		}
	}
}
