SWAGGER=java -jar ~/swagger/swagger-codegen-cli-2.3.1.jar
SPEC=replica.yml

all: generate requirements run
	@echo "DONE"

generate:
	$(SWAGGER) generate \
		-i $(SPEC) \
		-l python-flask \
		-o server/replica/flaskConnexion \
		-D supportPython2=true
	cp *_controller.py server/replica/flaskConnexion/swagger_server/controllers/  

run:
	cd server/replica/flaskConnexion/ &&\
	python -m swagger_server

requirements:
	pip install -r requirements.txt
	cd server/replica/flaskConnexion; pip install -r requirements.txt

clean:
	rm -rf server/