FROM ubuntu  

# just helps python run a little faster
ENV PYTHONBUFFER=1

RUN apt update && \
    apt ugrade -y && \
    
    pip3 install numpy pandas