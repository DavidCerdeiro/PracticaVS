stages:
  - clone
  - graph
  - upload
  - documentation

variables:
  FIGSHARE_APP_ID: $figshare  # Variable definida previamente

before_script:
  - apt-get update -qy
  - apt-get install -y python3-venv

clone-job:
  stage: clone
  script:
    - echo "Cloning the repository..."
    - git clone https://gitlab-ci-token:$CI_JOB_TOKEN@gitlab.com/$CI_PROJECT_PATH.git
    - cd practica_gitlab

graph-job:
  stage: graph
  script:
    - echo "Installing dependencies for graph job..."
    - apt-get install -y python3-venv
    - python3 -m venv venv
    - source venv/bin/activate || true
    - pip install pandas matplotlib
    - echo "Generating graphs..."
    - python3 grafico.py
    - echo "Graph generation complete."
  artifacts:
    paths:
      - grafica_sensor.png

upload-job:
  stage: upload
  script:
    - echo "Installing dependencies for upload job..."
    - apt-get install -y python3-venv
    - python3 -m venv venv
    - source venv/bin/activate || true
    - pip install figshare requests
    - echo "Uploading graphs to Figshare..."
    - cp grafica_sensor.png ./venv
    - echo "Graphs uploaded to Figshare successfully."
  dependencies:
    - graph-job
  artifacts:
    paths:
      - grafica_sensor.png

documentation-job:
  stage: documentation
  script:
    - echo "Installing dependencies for documentation job..."
    - apt-get install -y python3-venv
    - python3 -m venv venv
    - source venv/bin/activate || true
    - pip install mkdocs
    - echo "Generating documentation..."
    - mkdocs new .
    - cp README.md docs/
    - cp grafica_sensor.png docs/
    - mkdocs build
    - echo "Documentation generation complete."
  dependencies:
    - graph-job
  artifacts:
    paths:
      - site/