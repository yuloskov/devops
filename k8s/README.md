# LAB 9
## Step 5
```
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-69c8749775-8vtlb   1/1     Running   0          5m38s

NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/app-python   LoadBalancer   10.102.165.159   <pending>     5000:31056/TCP   2m49s
service/kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP          8m1s
```

## Step 9
NAME                                         READY   STATUS    RESTARTS        AGE
pod/app-python-deployment-77d74db5c8-cpthz   1/1     Running   1 (7m53s ago)   13m
pod/app-python-deployment-77d74db5c8-jwvcq   1/1     Running   1 (7m53s ago)   13m
pod/app-python-deployment-77d74db5c8-vq42m   1/1     Running   1 (7m53s ago)   13m

NAME                         TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/app-python-service   LoadBalancer   10.107.71.238   <pending>     5000:30721/TCP   4m21s
service/kubernetes           ClusterIP      10.96.0.1       <none>        443/TCP          37m