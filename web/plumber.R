#
# This is a Plumber API. You can run the API by clicking
# the 'Run API' button above.
#
# Find out more about building APIs with Plumber here:
#
#    https://www.rplumber.io/
#

library(plumber)

QB_RF <- readRDS("data/QB_RF.rds")
WR_RF <- readRDS("data/WR_RF.rds")
RB_RF <- readRDS("data/RB_RF.rds")


#* @apiTitle Plumber Example API
#* @apiDescription Plumber example description.

#* Echo back the input
#* @param msg The message to echo
#* @get /echo
function(msg = "") {
    list(msg = paste0("The message is: '", msg, "'"))
}

#* Predict QB Salary From Input
#* @param Rate
#* @param QBR
#* @param Cmp.
#* @param TD
#* @param Yds
#* @get /api/QB_RF
function(Rate, QBR, Cmp., TD, Yds) {
  list(prediction = predict(QB_RF, newdata = data.frame(
    Rate = as.numeric(Rate),
    QBR = as.numeric(QBR),
    Cmp. = as.numeric(Cmp.),
    TD = as.numeric(TD),
    Yds = as.numeric(Yds),
    Year = 2025
  )))
}

#* Predict RB Salary From Input
#* @param Y.G.Rush
#* @param Y.G.Rec
#* @param Total.Yds
#* @param T.G
#* @param Rec
#* @param Age
#* @get /api/RB_RF
function(Y.G.Rush, Y.G.Rec, Total.Yds, T.G, Rec, Age) {
  list(prediction = predict(RB_RF, newdata = data.frame(
    Y.G.Rush = as.numeric(Y.G.Rush),
    Y.G.Rec = as.numeric(Y.G.Rec),
    Total.Yds = as.numeric(Total.Yds),
    T.G = as.numeric(T.G),
    Rec = as.numeric(Rec),
    Age = as.numeric(Age),
    Year = 2025
  )))
}

#* Predict WR Salary From Input
#* @param R.G
#* @param Y.G
#* @param TD
#* @get /api/WR_RF
function(R.G, Y.G, TD) {
  list(prediction = predict(QB_RF, newdata = data.frame(
    R.G = as.numeric(R.G),
    Y.G = as.numeric(Y.G), 
    TD = as.numeric(TD),
    Year = 2025
  )))
}

# Programmatically alter your API
#* @plumber
function(pr) {
    pr %>%
        # Overwrite the default serializer to return unboxed JSON
        pr_set_serializer(serializer_unboxed_json()) %>%
        pr_set_docs(TRUE) %>%
        pr_static("/", "static")
        
}