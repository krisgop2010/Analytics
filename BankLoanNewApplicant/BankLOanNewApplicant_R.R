library(foreign)
dataset_german = read.spss("C:\\DataSets\\GermanCredit.sav", to.data.frame = TRUE)
rm(bulb_data)
rm(car)
rm(car_mixed)
rm(car_test)
rm(car_train)
rm(datamixed)
rm(dataset)
View(dataset_german)
View(dataset_german)
dataset_newapplicant = read.spss("C:\\DataSets\\NewApplicants.sav", to.data.frame = TRUE)
View(dataset_newapplicant)
View(dataset_newapplicant)
prop.table(dataset_german$CREDIT)
summary(dataset_german$CREDIT)
summary(dataset_german)
sapply(dataset_german, function(x) sum(is.na(x)))
str(dataset_german)
summary(dataset_german)
str(dataset_german)
boxplot(dataset_german$DURATION)
boxplot(dataset_german$DURATION)
boxplot(dataset_german$DURATION)
dataset_german_subset1 <- subset(dataset_german, dataset_german$DURATION<40)
boxplot(dataset_german_subset1$DURATION)
summary(dataset_german_subset1)
view(dataset_german_subset1)
View(dataset_german_subset1)
boxplot(dataset_german$DURATION)
dataset_german_subset1 <- subset(dataset_german, dataset_german$DURATION<45)
boxplot(dataset_german_subset1$DURATION)
summary(dataset_german_subset1)
str(dataset_german_subset1)
str(dataset_german)
dataset_german_subset1 <- subset(dataset_german, dataset_german$DURATION<50)
boxplot(dataset_german_subset1$DURATION)
summary(dataset_german_subset1)
str(dataset_german)
str(dataset_german_subset1)
boxplot(dataset_german$NUM_CREDITS)
table(dataset_german_subset1$CREDIT)
library(gmodels)
CrossTable(dataset_german_subset1$CREDIT_USE, dataset_german_subset1$CREDIT)
tabl1 <- table(dataset_german_subset1$CREDIT_USE, Home_Loan_dataset_german_subset1SubSet3$CREDIT)
tabl1 <- table(dataset_german_subset1$CREDIT_USE, dataset_german_subset1$CREDIT)
tabl1
tabl1 <- table(dataset_german_subset1$CREDIT_USE, dataset_german_subset1$CREDIT)
tabl1
chi2 = chisq.test(dataset_german_subset1$CREDIT_USE, dataset_german_subset1$CREDIT)
chi2
summary(dataset_german_subset1)
str(dataset_german_subset1)
summary(dataset_german_subset1)
tabl2 <- table(dataset_german_subset1$CREDIT_USE, dataset_german_subset1$CREDIT)
tabl2
chi2 = chisq.test(dataset_german_subset1$CREDIT_USE, dataset_german_subset1$CREDIT)
chi2
tabl3 <- table(dataset_german_subset1$NEW_CAR, dataset_german_subset1$CREDIT)
tabl3
chi3 = chisq.test(dataset_german_subset1$NEW_CAR, dataset_german_subset1$CREDIT)
chi3
tabl4 <- table(dataset_german_subset1$USED_CAR, dataset_german_subset1$CREDIT)
tabl4
chi4 = chisq.test(dataset_german_subset1$USED_CAR, dataset_german_subset1$CREDIT)
chi4
str(dataset_german_subset1)
tabl5 <- table(dataset_german_subset1$FURNITURE, dataset_german_subset1$CREDIT)
tabl5
chi5 = chisq.test(dataset_german_subset1$FURNITURE, dataset_german_subset1$CREDIT)
chi5
str(dataset_german_subset1)
tabl6 <- table(dataset_german_subset1$RADIOTV, dataset_german_subset1$CREDIT)
tabl6
chi6 = chisq.test(dataset_german_subset1$RADIOTV, dataset_german_subset1$CREDIT)
chi6
str(dataset_german_subset1)
tabl7 <- table(dataset_german_subset1$EDUCATION, dataset_german_subset1$CREDIT)
tabl7
chi7 = chisq.test(dataset_german_subset1$EDUCATION, dataset_german_subset1$CREDIT)
chi7
str(dataset_german_subset1)
tabl8 <- table(dataset_german_subset1$RETRAINING, dataset_german_subset1$CREDIT)
tabl8
chi8 = chisq.test(dataset_german_subset1$RETRAINING, dataset_german_subset1$CREDIT)
chi8
str(dataset_german_subset1)
tabl9 <- table(dataset_german_subset1$SAV_ACCT, dataset_german_subset1$CREDIT)
tabl9
chi9 = chisq.test(dataset_german_subset1$SAV_ACCT, dataset_german_subset1$CREDIT)
chi9
str(dataset_german_subset1)
tabl10 <- table(dataset_german_subset1$EMPLOYMENT, dataset_german_subset1$CREDIT)
tabl10
chi10 = chisq.test(dataset_german_subset1$EMPLOYMENT, dataset_german_subset1$CREDIT)
chi10
str(dataset_german_subset1)
tabl10 <- table(dataset_german_subset1$MALE_DIV, dataset_german_subset1$CREDIT)
tabl11 <- table(dataset_german_subset1$MALE_DIV, dataset_german_subset1$CREDIT)
tabl11
chi11 = chisq.test(dataset_german_subset1$MALE_DIV, dataset_german_subset1$CREDIT)
chi11
str(dataset_german_subset1)
tabl12 <- table(dataset_german_subset1$GUARANTOR, dataset_german_subset1$CREDIT)
tabl12
chi12 = chisq.test(dataset_german_subset1$GUARANTOR, dataset_german_subset1$CREDIT)
chi12
str(dataset_german_subset1)
tabl13 <- table(dataset_german_subset1$PRESENT_RESIDENT, dataset_german_subset1$CREDIT)
tabl13
chi13 = chisq.test(dataset_german_subset1$PRESENT_RESIDENT, dataset_german_subset1$CREDIT)
chi13
str(dataset_german_subset1)
tabl14 <- table(dataset_german_subset1$REAL_ESTATE, dataset_german_subset1$CREDIT)
tabl14
chi14 = chisq.test(dataset_german_subset1$REAL_ESTATE, dataset_german_subset1$CREDIT)
chi14
str(dataset_german_subset1)
str(dataset_german_subset1)
library(caTools)
library(caTools)
set.seed(123)# random seed
split = sample.split(dataset_german_subset1$CREDIT, SplitRatio = 0.75) # it returns true if the observation goes to training set, if it goes to test set, then it returns false
training_set = subset(dataset_german_subset1, split == TRUE)
test_set = subset(dataset_german_subset1, split == FALSE)
model = glm(formula = CREDIT ~ .,
            family = binomial(link = 'logit'),
            data = training_set,
            control = list(maxit = 50))
str(dataset_german_subset1)
test_set[-32]
test_set[-31]
test_set[-1]
test_set
str(test_set)
test_set[-32]
test_set[-33]
prob_pred = predict(model, type = 'response', newdata = test_set[-33])
prob_pred
y_pred = ifelse((prob_pred > 0.5), 1, 0)
y_pred
test_set[, 33]
cm = table(test_set[, 33], y_pred)
cm
library(ROCR)
pr = prediction(prob_pred, test_set$CREDIT)
prf = performance(pr, measure = "tpr", x.measure = "fpr")
plot(prf)
auc = performance(pr, measure = "auc")
auc = auc@y.values[[1]]
auc
View(dataset_newapplicant)
View(dataset_newapplicant)
str(dataset_newapplicant)
summary(model)
str(dataset_german_subset1)
model1 = glm(formula = CREDIT ~ CHK_ACCT + DURATION + HISTORY + CREDIT_USE + SAV_ACCT + INSTALL_RATE + OTHER_INSTALL,
             family = binomial(link = 'logit'),
             data = training_set,
             control = list(maxit = 50))
prob_pred = predict(model1, type = 'response', newdata = test_set[-33])
prob_pred
prob_pred1 = predict(model1, type = 'response', newdata = test_set[-33])
prob_pred1
y_pred1 = ifelse((prob_pred1 > 0.5), 1, 0)
y_pred1
cm1 = table(test_set[, 33], y_pred1)
cm1
library(ROCR)
pr1 = prediction(prob_pred1, test_set$CREDIT)
prf1 = performance(pr1, measure = "tpr", x.measure = "fpr")
plot(prf1)
auc1 = performance(pr1, measure = "auc")
auc1 = auc1@y.values[[1]]
auc1
auc
dataset_newapplicant$pred <- predict(model, newdata=dataset_newapplicant, type='response')
view(dataset_newapplicant)
View(dataset_newapplicant)
prob_pred1
dataset_newapplicant$credit_pred = ifelse((dataset_newapplicant$pred > 0.5), 'Yes', 'No')
View(dataset_newapplicant)
View(dataset_german)
View(dataset_german)
names(dataset_german_subset1)
View(dataset_newapplicant)
View(dataset_german_subset1)
View(dataset_german)
savehistory("~/Desktop/Banking.Rhistory")
savehistory("~/Desktop/rb1.Rhistory")
