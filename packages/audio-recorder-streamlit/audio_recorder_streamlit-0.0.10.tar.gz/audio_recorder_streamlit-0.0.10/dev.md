# Development mode
## Test local dev version
```sh
pdm dev-backend
pdm dev
```

## Test local built version
```sh
pdm start
```

## Deploy new version
Update version in `pyproject.toml` then:

```sh
pdm deploy-test
```

## Test deployed version
```sh
pdm venv create --name test-env 3.8
eval $(pdm venv activate test-env)
pip install "streamlit >= 0.63" "altair<5"  # for pypi-test only
pip install -i https://test.pypi.org/simple/ audio-recorder-streamlit==X.X.X
# OR
pip install audio-recorder-streamlit==X.X.X
deactivate
pdm venv remove test-env
```