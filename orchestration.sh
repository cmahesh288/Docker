kubectl apply -f docker-project-deployment.yaml

kubectl get deployments
kubectl get pods

kubectl get pods > kube_output.txt

cat kube_output.txt