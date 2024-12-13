# Running MediaCat in Docker

To run MediaCat in Docker, follow these steps:

1. **Create a working directory** and pull down the repository.

2. **Build the docker image** by running:

   ```bash
   docker build -t zstall/mediacat-flask-app:latest .
   ```

3. **Start the Docker containers** by running:

   ```bash
   docker compose up -d
   ```

4. Once the containers are running, **open a browser and go to localhost:5000** and click on the login link:

   ![alt text](https://github.com/zstall/mediacat-sqlalchemy/blob/main/localhostclicklogin.png?raw=true)


5. **Exec into the non-DB container**:

   ```bash
   docker exec -it <container-id> sh
   ```

6. In the container command line, **run the following command to create the necessary tables**:

   ```bash
   psql postgresql://admin:admin@<postgres-container-id>:5432/mediacat -af mediacat.sql
   ```

7. To populate the DB and create an admin user, **run the following in the non-DB container**:

   ```bash
   python3 create_mediacat_db.py
   ```

## Accessing the Application

This is a demo application and will be running on `localhost:5000`. To log in to the application, use:

- **Username**: `admin`
- **Password**: `admin`

**NOTE**: The Docker image can be found here: [https://hub.docker.com/repository/docker/zstall/mediacat-flask-app/general](https://hub.docker.com/repository/docker/zstall/mediacat-flask-app/general)
