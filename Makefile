MODULE := aveti

run-client:
	@python3 -m $(MODULE).client.main_window

grpc-gen:
	@python3 -m grpc_tools.protoc \
			-I $(MODULE)/interface \
			--python_out=./$(MODULE)/generated \
			--grpc_python_out=./$(MODULE)/generated \
			./$(MODULE)/interface/*.proto
	@sed -i -E 's/^\(import.*_pb2\)/from . \1/' ./$(MODULE)/generated/*.py