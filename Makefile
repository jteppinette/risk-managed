VENV_DIR     = venv
VENV_BIN_DIR = $(VENV_DIR)/bin

TARGET_DIR   = target

NAME = risk_managed

APPLICATION_BINARY       = $(NAME).pex
APPLICATION_ARCHIVE_FILE = $(NAME).tgz

.PHONY: build
build:
	virtualenv $(VENV_DIR)

	$(VENV_BIN_DIR)/pip install pex
	$(VENV_BIN_DIR)/pip wheel --wheel-dir=$(TARGET_DIR) --no-deps .
	$(VENV_BIN_DIR)/pex --output-file=$(TARGET_DIR)/$(APPLICATION_BINARY) \
			    --requirement=requirements.txt \
			    --find-links=$(TARGET_DIR) \
			    --disable-cache \
			    --console-script=$(NAME) \
			    --ignore-errors \
			    $(NAME)

	tar -czf $(TARGET_DIR)/$(APPLICATION_ARCHIVE_FILE) -C $(TARGET_DIR) $(APPLICATION_BINARY)
