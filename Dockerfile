FROM lsiobase/alpine.python
MAINTAINER j0nnymoe

# copy local files
COPY root/ /

# install packages and chmod execs
RUN \
 apk add --no-cache \
	curl \
	iptables \
	openvpn && \

 chmod +x /usr/bin/transmission-update.py

# ports and volumes
VOLUME /config
