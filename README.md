# Django/Rest with VueJS

### Installation

Clone the repository, then

```bash
make install
```

```bash
make
``` 

### Local Development

Create a superuser

```bash
make superuser
```

Open 2 terminals and then type

```bash
make run-backend
```

```bash
make run-frontend
```

Backend will be served at *http://localhost:8000* and frontend will served at *http://localhost:8080*

### Test

**Backend**

```bash
make test
```

```bash
make coverage
```

### Deployment on docker

```bash
make dockerd
```

Application will be served at *http://ip-of-your-server:8000*