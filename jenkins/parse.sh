#!/bin/sh

wget -q 'http://m.ahmadullin:Sun$357D@10.113.136.32/download_trbs/snapshots/devel/san/5.5-unified-asan/latest/build.xml'
ks=$(cat *.xml | grep san-tizen-5.5-unified-asan_)
ks=$(echo $ks | cut -c5-41)
ks=$ks"_mobile-wayland-armv7l-tm1.ks"
echo ${ks}
rm -rf build*
