def create_dockerfile(path, name:str = "Dockerfile"):
    dockerfile_content = f"""
# Use an official Python runtime as a parent image
FROM python:latest

# Set the working directory in the container
WORKDIR /app

# Install git
RUN apt-get update && apt-get install -y git

# Copy the current directory contents into the container at /app
COPY . /app

# Install okik and its dependencies
RUN pip install --upgrade pip
# create a virtual environment
RUN python3 -m venv venv
# activate the virtual environment
RUN . venv/bin/activate
# install okik
RUN echo "Installing okik"
RUN pip install okik
# install okik cli
RUN echo "Installing okik cli"
RUN export PATH="$HOME/.local/bin:$PATH"
RUN apt-get clean && rm -rf /var/lib/apt/lists/*
# verify installation
RUN echo "Verifying installation"
RUN which okik
RUN echo "Initialising okik"
RUN okik init

# Upgrade pip and install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3000

# Run okik app
CMD ["okik", "server"]
    """
    with open(f"{path}/{name}", 'w') as file:
        file.write(dockerfile_content)
