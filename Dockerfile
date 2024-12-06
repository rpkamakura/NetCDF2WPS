FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends gfortran && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir numpy
RUN pip install --no-cache-dir pywinter
RUN pip install --no-cache-dir netCDF4

WORKDIR /app

# To keep the container running
CMD ["tail", "-f", "/dev/null"]
