requirements:
	pip install -r requirements.txt

build:              
	brane unpublish -f predict 1.0.0
	brane remove -f predict
	brane build container.yml
	brane push predict 1.0.0
