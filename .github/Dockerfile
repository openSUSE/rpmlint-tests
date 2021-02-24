FROM opensuse/tumbleweed

# erlang is required for some tests
# gcc-PIE is needed, because default GCC doesn't create PIE binaries and we don't want to trigger position-independent-executable-suggested
RUN zypper --color in -y --no-recommends shadow && PATH=/usr/sbin/:$PATH zypper --color in -y --no-recommends rpmlint-Factory-strict rpmlint-Factory rpmlint-mini rpmbuild git erlang gcc-PIE colordiff
COPY integration_test.sh /integration_test.sh

ENTRYPOINT ["/integration_test.sh"]
