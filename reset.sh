#!/bin/bash
sed -i '/export LEVEL=/d' ~/.profile && unset LEVEL
