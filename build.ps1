micromamba create -n queryActivation -y "python<3.12"
micromamba activate

python -m pip install -r requirements.txt
python -m pip install pyinstaller

pyinstaller -D -y --optimize=2 -n query-batch query-batch.py
Copy-Item -Recurse db dist/query-batch
pyinstaller -D -y --optimize=2 -n query-single query-single.py
Copy-Item -Recurse db dist/query-single

Remove-Item -Force -Recurse build
Remove-Item *.spec
