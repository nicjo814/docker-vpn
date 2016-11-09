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

 chmod +x /usr/bin/transmission-update.py && \
 chmod +x /usr/bin/ovpn-up.sh && \
 chmod +x /usr/bin/ovpn-down.sh

# ports and volumes
VOLUME /config
