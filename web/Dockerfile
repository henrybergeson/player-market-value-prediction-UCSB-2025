FROM rocker/r-ver:4.3.1

RUN R -e "install.packages('plumber')"

COPY plumber.R /plumber.R

EXPOSE 8000

ENTRYPOINT ["R", "-e", "pr <- plumber::plumb('/plumber.R'); pr$run(host='0.0.0.0', port=8000)"]

