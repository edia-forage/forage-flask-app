
##  Deploy flask app to GKE using GitHub Actions

    1) Configure GCP details in github repo
    
            Project id - Add github secret name GKE_PROJECT
            Service Account - Add github secret name GKE_SA_KEY
    
    2) Configure k8 objects with GCP Infra details (pre-created)
    
            deployment.yml 
            - For gke-test container, configure DB credentials in secret "postgres-secret"
            - For side car, configure CloudSQL connection name in command
            
    3) Setup gitactions (Reference: https://github.com/google-github-actions/setup-gcloud/blob/master/example-workflows/gke/README.md)
     
            gke.yml
            - Set GKE_ZONE 
            - Set triggers based on requirement
        
    4) Configure SQLALCHEMY_DATABASE_URI to localhost as we use CLoud SQL Proxy side car
    
            127.0.0.1:5432

##  Validate deployment

    1) Check status on github actions
    
    2) Verify k8 objects
    
            gcloud container clusters get-credentials <cluster name> --region=<cluster region>
            kubectl get namespace
            kubectl get pod
            kubectl get services  (use external ip to access)
            kubectl logs [POD] -c gke-test
 
    3) Access application :-) 
    
            GET at http://<external ip shown by service>/
            POST at http://<external ip shown by service>/
    

