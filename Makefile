requirements:
	pip install -r requirements.txt

build:              
	brane unpublish -f predict
	brane remove -f predict
	brane build container.yml
	brane push predict