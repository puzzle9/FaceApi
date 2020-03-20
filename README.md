# FaceApi

# Install

- maybe sometimes install is boooooooooooom / restart

## aarch64

<https://pypi.org/project/numpy-aarch64/#files>
<https://pillow.readthedocs.io/en/latest/installation.html#building-on-linux>

## start

```
virtualenv --no-site-packages face_api
source bin/activate
```

## config

```
cp config.example.py config.py
cp uwsgi.example.ini uwsgi.ini
```

## pip

```
pip install -r requirement.txt
```

## sqlite

```bash
python sql.py
```

# server

## uwsgi

```
uwsgi uwsgi.ini
```

## supervisord

- more.


# Api

[Api](./API.md)

# Thanks

<https://github.com/ageitgey/face_recognition>

<https://github.com/peterjpxie/face_rec_api>
