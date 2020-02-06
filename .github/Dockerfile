FROM opensuse/tumbleweed

RUN zypper in -y --no-recommends rpmlint-Factory-strict rpmlint-Factory rpmlint-mini rpmbuild git erlang
COPY integration_test.sh /integration_test.sh

ENTRYPOINT ["/integration_test.sh"]
