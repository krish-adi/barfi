# Development notes

Following are the notes for working on the development of the barfi.

## Quickstart for development

- In terminal 1
```shell
make serve
```

- In terminal 2
```shell
make run
```

## Requirements

- Ensure you have [Python 3.6+](https://www.python.org/downloads/), [Node.js](https://nodejs.org), and [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) installed.
- Clone this repo to a local folder.

## Python virtual environment

Create a new Python virtual environment:

```shell
$ python3 -m venv venv  # create venv
$ . venv/bin/activate   # activate venv
$ pip install streamlit # install streamlit
```

Run the components's Streamlit app:

```shell
$ . venv/bin/activate  # activate the venv you created earlier
$ streamlit run barfi/__init__.py  # run the root test
```

## Node environment

Install and initialize the component's frontend:

```shell
$ cd barfi/frontend
$ npm install    # Install npm dependencies
$ npm run serve  # Start the dev server
```

# Build and Deploy

```shell
pip install build twine
python -m build 
twine upload --verbose --skip-existing dist/*
```

## Checklist before building new package
- [ ] Run unittest by running `make test`
- [ ] Change `Node` to `Block` here `barfi/frontend/node_modules/@baklavajs/plugin-renderer-vue/dist/index.js` @ `this.contextMenu.items`
- [ ] Build the frontend: `cd frontend/` and run `npm run build`
- [ ] Set `release = True` in */barfi/__init__.py*
- [ ] Bump version number in `setup.py`
- [ ] Build package: `python -m build`
- [ ] Bump version number in `docs/source/conf.py` 
- [ ] Update docs if required.
- [ ] Upload to twine using `make upload`
- [ ] Change Set `release = False` in */barfi/__init__.py*
- [ ] Update CHANGELOG
- [ ] Commit the repository with the version number `v 0.4.2`

## Resources

- https://stackoverflow.com/questions/1301346/what-is-the-meaning-of-single-and-double-underscore-before-an-object-name
- https://stackoverflow.com/questions/972/adding-a-method-to-an-existing-object-instance
- https://stackoverflow.com/questions/52799985/python-change-bound-method-to-another-method
- https://docs.python.org/3/tutorial/classes.html