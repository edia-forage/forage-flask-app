
##  Deploy flask app to GKE using GitHub Actions

    1) Configure GCP details in github repo
    
            Project id - Add it as github secret with name GKE_PROJECT
            Service Account - Add it as github secret with name GKE_SA_KEY
    
    2) Configure k8 objects with GCP Infra details (pre-created)
    
            deployment.yml 
            - For gke-test container, configure DB credentials in secret "postgres-secret"
            - For side car, configure CloudSQL connection name in command
            - For side car, map k8 secret "cloudsql-sa" to volume "sa-volume" at mountPath "/secrets/"
            
            If for some reason you want a new service
                kubectl expose deployment gke-test --type=LoadBalancer --port 80 --target-port 8080
            
    3) Setup gitactions (Reference: https://github.com/google-github-actions/setup-gcloud/blob/master/example-workflows/gke/README.md)
     
            gke.yml
            - Set GKE_ZONE 
            - Change triggers based on requirement (here we trigger for evey merge/push to main branch)
                on>push>branches
        
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
            kubectl exec [POD] -- [COMMAND]
 
    3) Access application :-) 
    
            GET at http://<external ip shown by service>/
            POST at http://<external ip shown by service>/
    

##  Local setup 

###  Setup postgresql locally
        Install postgresql from https://postgresapp.com/
        create a DB as below [terminal] 
            psql
            create database demo_user;
            \q
    
###  Create table by using SQLALCHEMY's migrate feature
    
        export SQLALCHEMY_DATABASE_URI="postgresql:///demo_user" 
        python manage.py db init
        python manage.py db migrate
        python manage.py db upgrade  (to apply changes)
        python initial_data_load.py  (to insert some sample data)
   
    
###  Check table data manually [terminal]
        psql
        \c demo_user
        \dt
        select * from demo_users;
    
###  Test running flask app locally
    
        python -m flask run (Dont use flask run as it triggers cli.py from outside of venv)
        Check at http://127.0.0.1:5000/ either through Postman for POST and GET 
    
        or run gunicorn
        gunicorn app:app
        Check at  http://127.0.0.1:8000/