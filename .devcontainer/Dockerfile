FROM python:3.12.8-bookworm

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=${USER_UID}
ARG POETRY_VERSION=2.1.4

RUN apt-get update \
  && apt-get install --yes --no-install-recommends git ca-certificates build-essential \
  && rm -rf /var/lib/apt/lists/*

RUN if ! getent group ${USER_GID}; then groupadd --gid ${USER_GID} ${USERNAME}; fi \
  && if ! id -u ${USERNAME} >/dev/null 2>&1; then useradd --uid ${USER_UID} --gid ${USER_GID} -m ${USERNAME}; fi

ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV POETRY_VERSION=${POETRY_VERSION}

RUN python3 -m pip install --no-cache-dir poetry==${POETRY_VERSION}

USER ${USERNAME}
WORKDIR /workspaces/ha-json-sqlite-store
