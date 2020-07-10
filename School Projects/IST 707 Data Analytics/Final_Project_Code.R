#set working directory
setwd("~/School/IST 707/Final Project")

#read in data
df <- read.csv("ksdata.csv",na.string = c(''),stringsAsFactors = FALSE) 

#libraries
library(ggplot2)
library(scales)
library(plyr)
library(lubridate)
library(reshape2)
library(RColorBrewer)

#################### CLEAN DATA #####################

#get rid of unneccessary columns
df$currency <- NULL
df$goal <- NULL
df$pledged <- NULL
df$usd.pledged <- NULL
df$ID <- NULL


#get rid of unneccessary rows
df <- df[!(df$country=='N,0"'),]
df <- df[!(df$state=="live"),]

#redefine state column
df$state[df$state=="canceled"] <- "failed"
df$state[df$state=="suspended"] <- "failed"

#replace NAs in "name" column
df[is.na(df)] <- "No name"

#change data types
df$name <- as.character(df$name)
df$state <- as.factor(df$state)
df$country <- as.factor(df$country)
df$category <- as.factor(df$category)
df$main_category <- as.factor(df$main_category)
df$deadline <- as.Date(df$deadline, tryFormats = "%m/%d/%Y")
df$launched <- as.Date(df$launched, tryFormats = "%m/%d/%Y")
df <- df[!(df$launched <= "2009-01-01"),]

#create new columns
#gap = money left to raise
df$gap <- df$usd_goal_real - df$usd_pledged_real
#days left = total days to fundraise
df$daystoraise <- difftime(df$deadline, df$launched, units = c("days"))
df$daystoraise <- as.integer(df$daystoraise)
df$launchmonth <- format(df$launched, "%B")
df$launchyear <- year(df$launched)
df$launchmonth <- as.factor(df$launchmonth)
df$launchyear <- as.factor(df$launchyear)

#################### PLOTS ##############################

average_campaign_length <- mean(df$deadline-df$launched)
average_campaign_length
average_goal_amount <- median(df$usd_goal_real)
average_goal_amount
average_pledge_amount <- median(df$usd_pledged_real)
average_pledge_amount

bestmonth <- count(df$launchmonth)


df.goal <- aggregate(df$usd_goal_real,by=list(df$main_category),FUN=median)

#review and assess
summary(df)
str(df)
sum(is.na(df))

#subset data

df.09 <- df[df$launched <= "2009-12-31",]
df.10 <- df[df$launched > "2009-12-31" & df$launched <= "2010-12-31",]
df.11 <- df[df$launched > "2010-12-31" & df$launched <= "2011-12-31",]
df.12 <- df[df$launched > "2011-12-31" & df$launched <= "2012-12-31",]
df.13 <- df[df$launched > "2012-12-31" & df$launched <= "2013-12-31",]
df.14 <- df[df$launched > "2013-12-31" & df$launched <= "2014-12-31",]
df.15 <- df[df$launched > "2014-12-31" & df$launched <= "2015-12-31",]
df.16 <- df[df$launched > "2015-12-31" & df$launched <= "2016-12-31",]
df.17 <- df[df$launched > "2016-12-31" & df$launched <= "2017-12-31",]
df.18 <- df[df$launched > "2017-12-31" & df$launched <= "2018-12-31",]
df.recent <- rbind(df.15,df.16,df.17)

#visualize

dfmelt <- reshape2::melt(df.recent, id=c("main_category","launchyear"),measure.vars = "gap",value.name = "gap")
dfmeltb <- reshape2::melt(df, id=c("main_category","launchyear"),measure.vars = "usd_pledged_real",value.name = "pledged")
dfmeltc <- reshape2::melt(df, id=c("main_category","state","launchyear"),measure.vars = "usd_pledged_real",value.name = "pledged")
dfmeltg <- reshape2::melt(df, id=c("main_category","state","launchyear"),measure.vars = "usd_goal_real",value.name = "goal")
dfmeltg2 <- reshape2::melt(df, id=c("usd_goal_real","state","launchyear"),measure.vars = "daystoraise",value.name = "campaignlength")
str(dfmelt)

dfmeltg_high <- dfmeltg[dfmeltg$goal >= 50000,]
dfmeltg_low <- dfmeltg[dfmeltg$goal < 50000,]

df_high <- count(dfmeltg_high, c("state","launchyear"))
df_low <- count(dfmeltg_low,c("state","launchyear"))
df_low <- df_low[(df_low$launchyear != "2018"),]

#plot df_high
plot_high <- ggplot(df_high, aes(x=launchyear,y=freq,fill=as.factor(state)))
plot_high <- plot_high + geom_bar(stat = "identity")
plot_high <- plot_high + scale_y_continuous(labels = comma)
plot_high <- plot_high + guides(fill=guide_legend(title="State"))
plot_high <- plot_high + ggtitle("Projects with $50K+ Goals") + xlab("Year") + ylab("# of projects") +
  theme(plot.title = element_text(hjust = 0.5))
plot_high

plot_low <- ggplot(df_low, aes(x=launchyear,y=freq,fill=as.factor(state)))
plot_low <- plot_low + geom_bar(stat = "identity")
plot_low <- plot_low + scale_y_continuous(labels = comma)
plot_low <- plot_low + guides(fill=guide_legend(title="State"))
plot_low <- plot_low + ggtitle("Projects with Goals Under $50K") + xlab("Year") + ylab("# of projects") +
  theme(plot.title = element_text(hjust = 0.5))
plot_low

dfmeltg2_long <- dfmeltg2[dfmeltg2$campaignlength >= 50,]
dfmeltg2_short <- dfmeltg2[dfmeltg2$campaignlength < 50,]

df_long <- count(dfmeltg2_long,c("state","launchyear"))
df_short <- count(dfmeltg2_short,c("state","launchyear"))
df_short <- df_short[(df_short$launchyear != "2018"),]

plot_long <- ggplot(df_long, aes(x=launchyear,y=freq,fill=as.factor(state)))
plot_long <- plot_long + geom_bar(stat = "identity")
plot_long <- plot_long + scale_y_continuous(labels = comma)
plot_long <- plot_long + guides(fill=guide_legend(title="State"))
plot_long <- plot_long + ggtitle("Projects Longer than 50 days") + xlab("Year") + ylab("# of projects") +
  theme(plot.title = element_text(hjust = 0.5))
plot_long

plot_short <- ggplot(df_short, aes(x=launchyear,y=freq,fill=as.factor(state)))
plot_short <- plot_short + geom_bar(stat = "identity")
plot_short <- plot_short + scale_y_continuous(labels = comma)
plot_short <- plot_short + guides(fill=guide_legend(title="State"))
plot_short <- plot_short + ggtitle("Projects Shorter than 50 days") + xlab("Year") + ylab("# of projects") +
  theme(plot.title = element_text(hjust = 0.5))
plot_short

dfmelt2 <- aggregate(dfmelt$gap,by=list(dfmelt$main_category,dfmelt$launchyear),FUN=sum)
colnames(dfmelt2)[colnames(dfmelt2)=="Group.1"] <- "Category"
colnames(dfmelt2)[colnames(dfmelt2)=="Group.2"] <- "Year"
colnames(dfmelt2)[colnames(dfmelt2)=="x"] <- "Gap"

dfmelt3 <- aggregate(dfmeltb$pledged,by=list(dfmeltb$launchyear),FUN=sum)
colnames(dfmelt3)[colnames(dfmelt3)=="Group.1"] <- "Year"
colnames(dfmelt3)[colnames(dfmelt3)=="x"] <- "Pledged"
dfmelt3$Year <- as.integer(dfmelt3$Year)
dfmelt3 <- dfmelt3[!(dfmelt3$Year == 2009 | dfmelt3$Year == 2018),]

dfmelt4 <- aggregate(dfmeltc$state,by=list(dfmeltc$main_category,df$state),FUN=length)
colnames(dfmelt4)[colnames(dfmelt4)=="Group.1"] <- "Category"
colnames(dfmelt4)[colnames(dfmelt4)=="Group.2"] <- "Status"
colnames(dfmelt4)[colnames(dfmelt4)=="x"] <- "StatusCount"

dfmelt_r = dfmelt2 %>% 
  group_by(Year) %>% 
  mutate(position = rank(-Gap))


# meltplot <- ggplot(dfmelt2, aes(x=Year, y=Gap, fill=as.factor(Category)))
# meltplot <- meltplot + geom_bar(stat = "identity",position=position_dodge())
# meltplot <- meltplot + scale_y_continuous(labels = comma)
# meltplot

#amount of funding not met, per category from 2015-2017
meltplot2 <- ggplot(dfmelt_r, aes(x=Year, y=Gap, fill=reorder(Category,-Gap, group = position)))
meltplot2 <- meltplot2 + geom_bar(stat = "identity",position=position_dodge())
meltplot2 <- meltplot2 + scale_y_continuous(labels = comma)
meltplot2

df.country1 <- aggregate(df$name,by=list(df$country),length)
plot1 <- ggplot(df.country1, aes(x=reorder(Group.1,-x),y=x,fill=as.factor(Group.1)))
plot1 <- plot1 + geom_bar(stat = "identity")
plot1 <- plot1 + scale_y_continuous(labels = comma)
plot1 <- plot1 + guides(fill=guide_legend(title="Year"))
plot1 <- plot1 + ggtitle("Number of Projects Per Country") + xlab("Year") + ylab("USD") +
  theme(plot.title = element_text(hjust = 0.5))
plot1

#amount pledged, per year
YearPlot <- ggplot(dfmelt3, aes(x=Year, y=Pledged, fill=as.factor(Year)))
YearPlot <- YearPlot + geom_bar(stat = "identity")
YearPlot <- YearPlot + scale_y_continuous(labels = comma)
# YearPlot <- YearPlot + scale_fill_gradient(labels = comma)
YearPlot <- YearPlot + guides(fill=guide_legend(title="Year"))
YearPlot <- YearPlot + ggtitle("Amount Pledged Per Year") + xlab("Year") + ylab("USD") +
  theme(plot.title = element_text(hjust = 0.5))
YearPlot

dfmelt_s = dfmelt4 %>% 
  group_by(Status) %>% 
  mutate(position = rank(-StatusCount))

meltplot2 <- ggplot(dfmelt_r, aes(x=Year, y=Gap, fill=reorder(Category,-Gap, group = position)))

#status of campaigns (failed or successful), by category
StatusPlot <- ggplot(dfmelt_s, aes(x=Status, y=StatusCount, fill=reorder(Category,-StatusCount, group = position)))
StatusPlot <- StatusPlot + geom_bar(stat = "identity",position=position_dodge())
StatusPlot <- StatusPlot + guides(fill=guide_legend(title="Category"))
StatusPlot <- StatusPlot + ggtitle("Status of Campaigns, by Category") + xlab("Status") + ylab("Number of Projects") +
  theme(plot.title = element_text(hjust = 0.5))
StatusPlot

df.failed <- df[df$state == "failed",]
df.f <- aggregate(df.failed$state,by=list(df.failed$main_category),FUN=length)
colnames(df.f)[colnames(df.f)=="Group.1"] <- "Category"
colnames(df.f)[colnames(df.f)=="x"] <- "Failed"
df.success <- df[df$state == "successful",]
df.s <- aggregate(df.success$state,by=list(df.success$main_category),FUN=length)
colnames(df.s)[colnames(df.s)=="Group.1"] <- "Category"
colnames(df.s)[colnames(df.s)=="x"] <- "Success"

df.status <- data.frame(cbind(Category=as.character(df.f$Category),Failed=df.f$Failed,
                              Success=df.s$Success))
df.status$Success <- as.integer(paste(df.status$Success))
df.status$Failed <- as.integer(paste(df.status$Failed))
str(df.status)
df.status$net <- df.status$Success - df.status$Failed
df.status$percent <- df.status$Success/(df.status$Failed+df.status$Success)

StatusPlot2 <- ggplot(df.status, aes(x=reorder(Category,-net), y=net, fill=net))
StatusPlot2 <- StatusPlot2 + geom_bar(stat="identity",position=position_dodge())
StatusPlot2 <- StatusPlot2 + theme(axis.text.x =
                                     element_text(size  = 10,
                                                  angle = 45,
                                                  hjust = 1,
                                                  vjust = 1))
StatusPlot2 <- StatusPlot2 + guides(fill=guide_legend(title="Net Success"))
StatusPlot2 <- StatusPlot2 + ggtitle("Net Success of Campaigns by Category") + xlab("Category") + ylab("Success") +
  theme(plot.title = element_text(hjust = 0.5))
StatusPlot2

StatusPlot3 <- ggplot(df.status, aes(x=reorder(Category,-percent), y=percent, fill=percent))
StatusPlot3 <- StatusPlot3 + geom_bar(stat="identity",position=position_dodge())
StatusPlot3 <- StatusPlot3 + theme(axis.text.x =
                                     element_text(size  = 10,
                                                  angle = 45,
                                                  hjust = 1,
                                                  vjust = 1))
StatusPlot3 <- StatusPlot3 + guides(fill=guide_legend(title="Percent Success"))
StatusPlot3 <- StatusPlot3 + ggtitle("Percent Success of Campaigns by Category") + xlab("Category") + ylab("% Success") +
  theme(plot.title = element_text(hjust = 0.5))
StatusPlot3

#df.mainc <- df[which(df$country == "US" | df$country == "CA" | df$country == "GB"),]
df.mainc <- df
countryplot <- ggplot(df.mainc, aes(x=country,fill=as.factor(country)))
countryplot <- countryplot + geom_bar()
countryplot <- countryplot + scale_y_continuous(labels = comma)
countryplot <- countryplot + ggtitle("Number of Projects by Country") + xlab("Country") + ylab("Number of Projects") +
  theme(plot.title = element_text(hjust = 0.5))
countryplot <- countryplot + guides(fill=guide_legend(title="Country"))
countryplot

df.m.failed <- df.mainc[df.mainc$state == "failed",]
df.m.f <- aggregate(df.m.failed$state,by=list(df.m.failed$country),FUN=length)
colnames(df.m.f)[colnames(df.m.f)=="Group.1"] <- "Country"
colnames(df.m.f)[colnames(df.m.f)=="x"] <- "Failed"
df.m.success <- df.mainc[df.mainc$state == "successful",]
df.m.s <- aggregate(df.m.success$state,by=list(df.m.success$country),FUN=length)
colnames(df.m.s)[colnames(df.m.s)=="Group.1"] <- "Country"
colnames(df.m.s)[colnames(df.m.s)=="x"] <- "Success"

df.m.status <- data.frame(cbind(Country=as.character(df.m.f$Country),Failed=df.m.f$Failed,
                              Success=df.m.s$Success))
df.m.status$Success <- as.integer(paste(df.m.status$Success))
df.m.status$Failed <- as.integer(paste(df.m.status$Failed))
df.m.status$net <- df.m.status$Success/(df.m.status$Failed+df.m.status$Success)

Net3C <- ggplot(df.m.status, aes(x=reorder(Country,-net),y=net,fill=as.factor(Country)))
Net3C <- Net3C + geom_bar(stat="identity",position=position_dodge())
Net3C <- Net3C + guides(fill=guide_legend(title="Country"))
Net3C <- Net3C + ggtitle("Overall Campaign Success by Country") + xlab("Country") + ylab("Percent") +
  theme(plot.title = element_text(hjust = 0.5))
Net3C

df.sumcat <- aggregate(df$usd_pledged_real,by=list(df$main_category),sum)
CategoryPlot <- ggplot(df.sumcat, aes(x=reorder(Group.1, x),y=x,fill=factor(Group.1)))
CategoryPlot <- CategoryPlot + geom_bar(stat="identity")
CategoryPlot <- CategoryPlot + theme(axis.text.x =
                       element_text(size  = 10,
                                    angle = 45,
                                    hjust = 1,
                                    vjust = 1))
CategoryPlot <- CategoryPlot + scale_y_continuous(labels = comma)
CategoryPlot <- CategoryPlot + guides(fill=guide_legend(title="Category"))
CategoryPlot <- CategoryPlot + ggtitle("Funding for Projects by Category, 2009-Jan 2018") + xlab("Category") + ylab("Total Funding") +
  theme(plot.title = element_text(hjust = 0.5))
CategoryPlot <- CategoryPlot + coord_flip()
CategoryPlot

df.sumproj <- aggregate(df$name,by=list(df$main_category),length)
Projectplot <- ggplot(df.sumproj, aes(x=reorder(Group.1,x),y=x,fill=as.factor(Group.1)))
Projectplot <- Projectplot + geom_bar(stat = "identity")
Projectplot <- Projectplot + scale_y_continuous(labels = comma)
Projectplot <- Projectplot + theme(axis.text.x =
                                       element_text(size  = 10,
                                                    angle = 45,
                                                    hjust = 1,
                                                    vjust = 1))
Projectplot <- Projectplot + ggtitle("Number of Projects by Category") + xlab("Category") + ylab("Number of Projects") +
  theme(plot.title = element_text(hjust = 0.5))
Projectplot <- Projectplot + guides(fill=guide_legend(title="Category"))
Projectplot <- Projectplot + coord_flip()
Projectplot

#################### ASSOCIATION RULE MINING #########################
library(arules)
library(arulesViz)

df_dis <- df
df_dis$name <- NULL
df_dis$deadline <- NULL
df_dis$launched <- NULL
df_dis$gap <- NULL
df_dis$backers <- NULL
df_dis$usd_pledged_real <- NULL
df_dis$usd_goal_real <- NULL
df_dis$launchyear <- as.factor(df_dis$launchyear)

summary(df_dis)


#discretize data
df_dis$usd_pledged_real <- cut(df_dis$usd_pledged_real, breaks = c(-Inf,100,500,1000,5000,10000,Inf),
                               labels=c("very low","low","average","high",
                                        "very high","extremely high"))

df_dis$usd_goal_real <- cut(df_dis$usd_goal_real, breaks = c(-Inf,1000,2500,5500,10000,50000,Inf),
                            labels=c("very low","low","average","high",
                                     "very high","extremely high"))

df_dis$backers <- cut(df_dis$backers, breaks = c(-Inf,0,1,6,12,50,100,Inf),
                      labels=c("none","one","a few","some","many",
                               "lots","tons"))

df_dis$daystoraise <- cut(df_dis$daystoraise, breaks = c(-Inf,5,15,30,45,60,Inf),
                       labels=c("a few days","several days","a few weeks","several weeks",
                                "almost two months","plenty of time"))

#First set of rules
KS_Rules <- apriori(df_dis, parameter = list(supp = 0.01, conf = 0.70, maxlen = 3),
                    appearance = list(default="lhs",rhs=c("state=successful","state=failed")))
KS_Rules <- sort(KS_Rules,by="lift",decreasing = TRUE)
inspect(KS_Rules[1:10])

plot(KS_Rules)

#Second set of rules
KS_Rules2 <- apriori(df_dis, parameter = list(supp = 0.05, conf = 0.60, maxlen = 3),
                    appearance = list(default="lhs",rhs=c("state=successful","state=failed")))
KS_Rules2 <- sort(KS_Rules2,by="lift",decreasing = TRUE)
inspect(KS_Rules2[1:10])

#Third set of rules


#################### DECISION TREEES #########################

library(rpart)
library(rpart.plot)
library(rattle)
library(caret)
library(RWeka)
library(e1071)

df_tree <- df
df_tree$gap <- NULL
df_tree$name <- NULL
df_tree$launched <- NULL
df_tree$deadline <- NULL
df_tree$usd_pledged_real <- NULL
df_tree$category <- NULL
every4_rows <- seq(1,nrow(df_tree),4)
DTsample_test <- df_tree[every4_rows,]
DTsample_train <- df_tree[-every4_rows,]

View(df_tree)

DTSmodeltest_nl   <- DTsample_test[-c(2)]
DTSmodeltest_jl <- DTsample_test$state

#Tree 1
Tree1 <- rpart(state ~.,DTsample_train,method = "class",control=rpart.control())
Tree1_predict <- predict(Tree1,DTSmodeltest_nl,type ="class")
confusionMatrix(Tree1_predict,DTSmodeltest_jl)


#plot
rpart.plot(Tree1,cex = .8,extra = 102, branch = 0,box.palette = 0,type = 2, branch.lty = 3)

#use printcp function to see how model performs - cross validation
printcp(Tree1)
bestcp <- Tree1$cptable[which.min(Tree1$cptable[,"xerror"]),"CP"]

#create rPart model 2 - pruned
Tree1.pruned <- prune(Tree1, cp = bestcp)
rpart.plot(Tree1.pruned,cex = .8,extra = 102, branch = 0,box.palette = 0,type = 2, branch.lty = 3)

#Tree 2
Tree2 <- rpart(state ~ launchmonth +launchyear + country + daystoraise,DTsample_train,method = "class",control=rpart.control())
Tree2_predict <- predict(Tree2,DTSmodeltest_nl,type ="class")
confusionMatrix(Tree2_predict,DTSmodeltest_jl)

#plot 2
rpart.plot(Tree2,cex = .8,extra = 102, branch = 0,box.palette = 0,type = 2, branch.lty = 3)

#Tree 3
Tree3 <- rpart(state ~ main_category,DTsample_train,method = "class",control=rpart.control())
Tree3_predict <- predict(Tree3,DTSmodeltest_nl,type ="class")
confusionMatrix(Tree3_predict,DTSmodeltest_jl)

#plot 
rpart.plot(Tree3,cex = .8,extra = 102, branch = 0,box.palette = 0,type = 2, branch.lty = 3)

#################### RANDOM FOREST #######################################

library(randomForest)
library(caret)

Forest <- randomForest(state~., data=DTsample_train,ntree=10)
Forest_predict <- predict(Forest,DTSmodeltest_nl,type ="class")
confusionMatrix(Forest_predict,DTSmodeltest_jl)

plot(randomForest(state~., data=DTsample_train,ntree=10),log="y")
varImpPlot(Forest,sort=TRUE)

Forest2 <- randomForest(state~usd_goal_real+backers+main_category+launchyear, data=DTsample_train,ntree=15)
Forest2_predict <- predict(Forest2,DTSmodeltest_nl,type ="class")
confusionMatrix(Forest2_predict,DTSmodeltest_jl)

plot(randomForest(state~., data=DTsample_train,ntree=10),log="y")
varImpPlot(Forest,sort=TRUE)

#################### WORDCLOUD #######################################

library(proxy)
library(tm)
library(network)
library(wordcloud)
library(quanteda)
library(qdap)
library(factoextra)
library(RColorBrewer)
library(FSelector)

df_s <- df[df$state == "successful",]
sample_df_s <- df_s[sample(nrow(df_s), 1000), ]
s_corpus <- Corpus(VectorSource(sample_df_s$name))
inspect(s_corpus)

#clean df_s corpus
s_corpus_clean <- tm_map(s_corpus, removePunctuation)
s_corpus_clean <- tm_map(s_corpus_clean, removeNumbers)
s_corpus_clean <- tm_map(s_corpus_clean, content_transformer(tolower))
# s_corpus_clean <- tm_map(s_corpus_clean, stemDocument)
s_corpus_clean <- tm_map(s_corpus_clean, removeWords, stopwords("english"))
s_corpus_clean <- tm_map(s_corpus_clean, stripWhitespace)
MyWords <- c("new","project","canceled")
s_corpus_clean <- tm_map(s_corpus_clean, removeWords, MyWords)

inspect(s_corpus_clean)

freq_terms(s_corpus_clean,50)

dtm_success <- TermDocumentMatrix(s_corpus_clean, control = list(
  weighting = weightTfIdf, normalize = TRUE,
  wordLengths=c(3,15)))

m_success <- as.matrix(dtm_success)
head(m_success)
v <- sort(rowSums(m_success),decreasing=TRUE)
d <- data.frame(word = names(v),freq=v)
head(d, 10)

set.seed(1234)
wordcloud(words = d$word, freq = d$freq, min.freq = 1,
          max.words=200, random.order=FALSE, rot.per=0.35, 
          colors=brewer.pal(8, "Dark2"))

df_f <- df[df$state == "failed",]
sample_df_f <- df_f[sample(nrow(df_f), 1000), ]
f_corpus <- Corpus(VectorSource(sample_df_f$name))

f_corpus_clean <- tm_map(f_corpus, removePunctuation)
f_corpus_clean <- tm_map(f_corpus_clean, content_transformer(tolower))
f_corpus_clean <- tm_map(f_corpus_clean, removeWords, stopwords("english"))
f_corpus_clean <- tm_map(f_corpus_clean, stripWhitespace)
MyWords <- c("new","project","canceled")
f_corpus_clean <- tm_map(f_corpus_clean, removeWords, MyWords)

# freq_terms(f_corpus_clean,50)

dtm_fail <- TermDocumentMatrix(f_corpus_clean, control = list(
  weighting = weightTfIdf, normalize = TRUE,
  wordLengths=c(3,15)))

m_fail <- as.matrix(dtm_fail)
head(m_fail)
vv <- sort(rowSums(m_fail),decreasing=TRUE)
dd <- data.frame(word = names(vv),freq=vv)
head(dd, 10)

set.seed(1234)
wordcloud(words = dd$word, freq = dd$freq, min.freq = 1,
          max.words=200, random.order=FALSE, rot.per=0.35, 
          colors=brewer.pal(8, "Dark2"))


#################### SVM on Text Mining #############
library(FSelector)

sample_df <- df[sample(nrow(df), 1500),]
Gain1 <- gain.ratio(state~.,data = sample_df)
Chisq <- FSelector::chi.squared(state~.,data = sample_df)

master_corpus <- Corpus(VectorSource(sample_df$name))
inspect(master_corpus)

#clean df_s corpus
m_corpus_clean <- tm_map(master_corpus, removePunctuation)
m_corpus_clean <- tm_map(m_corpus_clean, removeNumbers)
m_corpus_clean <- tm_map(m_corpus_clean, content_transformer(tolower))
# s_corpus_clean <- tm_map(s_corpus_clean, stemDocument)
m_corpus_clean <- tm_map(m_corpus_clean, removeWords, stopwords("english"))
m_corpus_clean <- tm_map(m_corpus_clean, stripWhitespace)
MyWords <- c("new","project","canceled")
m_corpus_clean <- tm_map(m_corpus_clean, removeWords, MyWords)

freq_terms(m_corpus_clean,20)

dtm_master <- DocumentTermMatrix(m_corpus_clean, control = list(
  weighting = weightTfIdf, normalize = TRUE,
  wordLengths=c(3,15)))

mm <- as.data.frame(as.matrix(scale(dtm_master)))
mmm <- cbind(sample_df$state,mm)
colnames(mmm)[colnames(mmm)== "sample_df$state"] <- "sstate"

every4_rows <- seq(1,nrow(mmm),4)
m_Test <- mmm[every4_rows,]
m_Train <- mmm[-every4_rows,]

mtest_nl <- m_Test[-c(1)]
mtest_jl <- as.factor(m_Test$sstate)

m_Train$sstate <- as.factor(m_Train$sstate)

library(e1071)
library(caret)

SVM1 <- svm(sstate~.,data = m_Train,kernel="linear")
SVM1_predict <- predict(SVM1,mtest_nl)
confusionMatrix(SVM1_predict,mtest_jl)




#################### NaiveBayes models ##########

df_cleaned <- df

############### Test and Training Sets

df_cleaned$name <- NULL
df_cleaned$category <- NULL
df_cleaned$deadline <- NULL
df_cleaned$launched <- NULL
df_cleaned$usd_pledged_real <- NULL
df_cleaned$gap <- NULL
df_cleaned$daysleft <- NULL

View(df_cleaned)

write.csv(df_cleaned, "df_cleaned.csv")

(every15_rows<-seq(1,nrow(df_cleaned),15))

(test_nb=df_cleaned[every15_rows, ])
nrow(test_nb)
(train_nb=df_cleaned[-every15_rows, ])
nrow(train_nb)
## View the created Test and Train sets
(head(train_nb))
(table(train_nb$state))
(table(train_nb$state))

## Make sure you take the labels out of the testing data
(head(test_nb))
nb_test_noLabel<-test_nb[-c(2)]
(nb_test_justLabel<-test_nb$state)
(head(nb_test_noLabel))
View(nb_test_noLabel)
View(nb_test_justLabel)

str(test_nb$state)

#### e1071
NB_e1071<-naiveBayes(state~., data = train_nb, na.action = na.pass)
NB_e1071_Pred <- predict(NB_e1071, nb_test_noLabel)
NB_e1071
table(NB_e1071_Pred,nb_test_justLabel) #confusion matrix
confusionMatrix(NB_e1071_Pred,nb_test_justLabel) #confusion matrix

############### 2nd NB RUN

## Create a test and train set - Used for first naive bayes run
## 47% of the sample size for test_set
smp_size_nb_test_2nd <- head(0.47 * nrow(df_cleaned))
## set the seed to make your partition reproducible
set.seed(19)
test_set_2nd <- sample(seq_len(nrow(df_cleaned)), size = smp_size_nb_test_2nd)
View(test_set_2nd)

#Split the data up between training and test data
(nb_test_2nd=df_cleaned[test_set_2nd, ])
nrow(nb_test_2nd)
(nb_train_2nd=df_cleaned[-test_set_2nd, ])
nrow(nb_train_2nd)

## View the created Test and Train sets
View(nb_train_2nd)
View(nb_test_2nd)

## Make sure you take the labels out of the testing data
(head(nb_test_2nd))
nb_test_noLabel_2nd<-nb_test_2nd[-c(2)]
(nb_test_justLabel_2nd<-nb_test_2nd$state)
(head(nb_test_noLabel_2nd))
View(nb_test_noLabel_2nd)

#### e1071
NB_e1071_2nd<-naiveBayes(state ~ backers + country + daystoraise, data = nb_train_2nd, na.action = na.pass)
NB_e1071_Pred_2nd <- predict(NB_e1071_2nd, nb_test_noLabel_2nd)
NB_e1071_2nd
table(NB_e1071_Pred_2nd,nb_test_justLabel_2nd) #confusion matrix
confusionMatrix(NB_e1071_Pred_2nd,nb_test_justLabel_2nd)

############### 3rd NB RUN

## Create a test and train set
(every7th_row<-seq(1,nrow(df_cleaned),3))

#Split the data up between training and test data
(nb_test_new=df_cleaned[every7th_row, ])
nrow(nb_test_new)
(nb_train_new=df_cleaned[-every7th_row, ])
nrow(nb_train_new)
## View the created Test and Train sets
(head(nb_train_new$state))

## View the created Test and Train sets
View(nb_train_new)
View(nb_test_new)

## Make sure you take the labels out of the testing data
(head(nb_test_new))
nb_test_noLabel_new<-nb_test_new[-c(2)]
(nb_test_justLabel_new<-nb_test_new$state)
(head(nb_test_noLabel_new))
View(nb_test_noLabel_new)

#### e1071
NB_e1071_3rd <-naiveBayes(state ~  main_category + launchyear + country + backers, data = nb_train_new, na.action = na.pass)
NB_e1071_Pred_3rd <- predict(NB_e1071_3rd, nb_test_noLabel_new)
NB_e1071_3rd
table(NB_e1071_Pred_3rd, nb_test_justLabel_new) #confusion matrix
confusionMatrix(NB_e1071_Pred_3rd,nb_test_justLabel_new)

############### 4th NB RUN

## Create a test and train set - Used for first naive bayes run
## 22% of the sample size for test_set
smp_size_nb_test_4th <- head(0.22 * nrow(df_cleaned))
## set the seed to make your partition reproducible
set.seed(52)
test_set_4th <- sample(seq_len(nrow(df_cleaned)), size = smp_size_nb_test_4th)
View(test_set_4th)

## Create a test and train set
(every4th_row<-seq(1,nrow(df_cleaned),4))

#Split the data up between training and test data
(nb_test_new4=df_cleaned[test_set_4th, ])
nrow(nb_test_new4)
(nb_train_new4=df_cleaned[-test_set_4th, ])
nrow(nb_train_new4)
## View the created Test and Train sets
(head(nb_train_new$state))

## View the created Test and Train sets
View(nb_train_new4)
View(nb_test_new4)

## Make sure you take the labels out of the testing data
(head(nb_test_new4))
nb_test_noLabel_new4<-nb_test_new4[-c(2)]
(nb_test_justLabel_new4<-nb_test_new4$state)
(head(nb_test_noLabel_new4))
View(nb_test_noLabel_new4)

#### e1071
NB_e1071_4th <-naiveBayes(nb_train_new4$state ~ main_category + usd_goal_real + launchmonth, data = nb_train_new4, na.action = na.pass)
NB_e1071_Pred_4th <- predict(NB_e1071_4th, nb_test_noLabel_new4)
NB_e1071_4th
table(NB_e1071_Pred_4th, nb_test_justLabel_new4) #confusion matrix
confusionMatrix(NB_e1071_Pred_4th,nb_test_justLabel_new4)

#Confusion Matrix - RESULTS

table(NB_e1071_Pred,nb_test_justLabel) #confusion matrix
table(NB_e1071_Pred_2nd,nb_test_justLabel_2nd) #confusion matrix
table(NB_e1071_Pred_3rd, nb_test_justLabel_new) #confusion matrix
table(NB_e1071_Pred_4th, nb_test_justLabel_new4) #confusion matrix

confusionMatrix(NB_e1071_Pred,nb_test_justLabel) #every 15th row, 54.13% accurate
confusionMatrix(NB_e1071_Pred_2nd,nb_test_justLabel_2nd) #47%/54% of data for set, 68.39% accurate
confusionMatrix(NB_e1071_Pred_3rd,nb_test_justLabel_new) #every 7th row, 68.60% accurate
confusionMatrix(NB_e1071_Pred_4th,nb_test_justLabel_new4) #22%/78% split, 39.98% accuracy

#################### SVM Model #########################

svm_cleaned <- df_cleaned

#svm_cleaned$state<-as.factor(svm_cleaned$state) 

svm_cleaned <- df_cleaned[sample(nrow(df_cleaned), 10000), ]

## Create a test and train set
## 15% of the sample size
smp_size_svm_cleaned <- floor(0.40* nrow(svm_cleaned))
## set the seed to make your partition reproducible
set.seed(12)
test_set_svm_cleaned <- sample(seq_len(nrow(svm_cleaned)), size = smp_size_svm_cleaned)
View(test_set_svm_cleaned)

(svm_test=svm_cleaned[test_set_svm_cleaned, ])
nrow(svm_test)
(svm_train=svm_cleaned[-test_set_svm_cleaned, ])
nrow(svm_train)

## View the created Test and Train sets
(head(svm_train))
(table(svm_train$state))
View(svm_train)
str(svm_train)
(head(svm_test))
(table(svm_test$state))
View(svm_test)
str(svm_test)

## Make sure you take the labels out of the testing data
(head(svm_test))
svm_test_noLabel<-svm_test[-c(2)]
(svm_test_justLabel<-svm_test$state)
(head(svm_test_noLabel))
View(svm_test_noLabel)
View(svm_test_justLabel)

(head(svm_train))
svm_train_noLabel<-svm_train[-c(2)]
(svm_train_justLabel<-svm_train$state)
(head(svm_train_noLabel))
View(svm_train_noLabel)
View(svm_train_justLabel)


## Polynomial Kernel... # 3 different costs to compare
SVM_fit_P_1st <- svm(state ~ backers + main_category + country, 
                     data=svm_train, 
                     kernel="polynomial", cost=.1, 
                     scale=FALSE)
print(SVM_fit_P_1st)

SVM_fit_P_2nd <- svm(state ~ backers + main_category + country + daystoraise, 
                     data=svm_train,
                     kernel="polynomial", cost=.5, 
                     scale=FALSE)
print(SVM_fit_P_2nd) 

SVM_fit_P_3rd <- svm(state ~ backers + main_category + country + launchyear, 
                     data=svm_train, 
                     kernel="polynomial", cost=1.0, 
                     scale=FALSE)
print(SVM_fit_P_3rd)

(pred_P_1st <- predict(SVM_fit_P_1st, svm_test, type="class"))
(pred_P_2nd <- predict(SVM_fit_P_2nd, svm_test, type="class"))
(pred_P_3rd <- predict(SVM_fit_P_3rd, svm_test, type="class"))

(Ptable_1st <- table(pred_P_1st, svm_test_justLabel))
(Ptable_2nd <- table(pred_P_2nd, svm_test_justLabel))
(Ptable_3rd <- table(pred_P_3rd, svm_test_justLabel))

#### Misclassifications
(MR_P <- 1 - sum(diag(Ptable_1st))/sum(Ptable_1st)) # Returns 63.80%
(MR_P <- 1 - sum(diag(Ptable_2nd))/sum(Ptable_2nd)) # Returns 27.65%
(MR_P <- 1 - sum(diag(Ptable_3rd))/sum(Ptable_3rd)) # Returns 31.27%

### Accuracy of model
confusionMatrix(pred_P_1st, svm_test_justLabel)
confusionMatrix(pred_P_2nd, svm_test_justLabel)
confusionMatrix(pred_P_3rd, svm_test_justLabel)

#Linear kernel - SVM

SVM_fit_L <- svm(state ~ backers + main_category + country, 
                 data=svm_train, 
                 kernel="linear", cost=.1, 
                 scale=FALSE)
print(SVM_fit_L)
(pred_L <- predict(SVM_fit_L, svm_test, type="class"))
(L_table<-table(pred_L, svm_test_justLabel))

SVM_fit_L_2nd <- svm(state ~ backers + main_category + country + daystoraise, 
                     data=svm_train, 
                     kernel="linear", cost=.5, 
                     scale=FALSE)
print(SVM_fit_L_2nd)
(pred_L_2nd <- predict(SVM_fit_L_2nd, svm_test, type="class"))
(L_table_2nd<-table(pred_L_2nd, svm_test_justLabel))

SVM_fit_L_3rd <- svm(state ~ backers + main_category + country + launchyear, 
                     data=svm_train, 
                     kernel="linear", cost=100.0, 
                     scale=FALSE)
print(SVM_fit_L_3rd)
(pred_L_3rd <- predict(SVM_fit_L_3rd, svm_test, type="class"))
(L_table_3rd<-table(pred_L_3rd, svm_test_justLabel))

(pred_P_4th <- predict(SVM_fit_L, svm_test, type="class"))
(pred_P_5th <- predict(SVM_fit_L_2nd, svm_test, type="class"))
(pred_P_6th <- predict(SVM_fit_L_3rd, svm_test, type="class"))

(Ptable_4th <- table(pred_P_4th, svm_test_justLabel))
(Ptable_5th <- table(pred_P_5th, svm_test_justLabel))
(Ptable_6th <- table(pred_P_6th, svm_test_justLabel))

#Miscalssifications
(MR_L <- 1 - sum(diag(L_table))/sum(L_table)) # Returns 18.33%
(MR_L_2nd <- 1 - sum(diag(L_table_2nd))/sum(L_table_2nd)) # Returns 17.88%
(MR_L_3rd <- 1 - sum(diag(L_table_3rd))/sum(L_table_3rd)) # Returns 22.63%

### Accuracy of model
confusionMatrix(pred_P_4th, svm_test_justLabel)
confusionMatrix(pred_P_5th, svm_test_justLabel)
confusionMatrix(pred_P_6th, svm_test_justLabel)


#Radial kernel - SVM

SVM_fit_R <- svm(state ~ backers + main_category + country, 
                 data=svm_train, 
                 kernel="radial", cost=10.0, 
                 scale=FALSE)
print(SVM_fit_R)
(pred_R <- predict(SVM_fit_R, svm_test, type="class"))
(R_table<-table(pred_R, svm_test_justLabel))

SVM_fit_R_2nd <- svm(state ~ backers + main_category + country + daystoraise, 
                     data=svm_train, 
                     kernel="radial", cost=100.0, 
                     scale=FALSE)
print(SVM_fit_R_2nd)
(pred_R_2nd <- predict(SVM_fit_R_2nd, svm_test, type="class"))
(R_table_2nd<-table(pred_R_2nd, svm_test_justLabel))

SVM_fit_R_3rd <- svm(state ~ backers + main_category + country + launchyear, 
                     data=svm_train, 
                     kernel="radial", cost=1000.0, 
                     scale=FALSE)
print(SVM_fit_R_3rd)
(pred_R_3rd <- predict(SVM_fit_R_3rd, svm_test, type="class"))
(R_table_3rd<-table(pred_R_3rd, svm_test_justLabel))

(pred_P_7th <- predict(SVM_fit_R, svm_test, type="class"))
(pred_P_8th <- predict(SVM_fit_R_2nd, svm_test, type="class"))
(pred_P_9th <- predict(SVM_fit_R_3rd, svm_test, type="class"))

### Confusion Matrix
(Ptable_7th <- table(pred_P_7th, svm_test_justLabel))
(Ptable_8th <- table(pred_P_8th, svm_test_justLabel))
(Ptable_9th <- table(pred_P_9th, svm_test_justLabel))

#Miscalssifications
(MR_R <- 1 - sum(diag(R_table))/sum(R_table)) # Returns 14.20%
(MR_R_2nd <- 1 - sum(diag(R_table_2nd))/sum(R_table_2nd)) # Returns 16.58%
(MR_R_3rd <- 1 - sum(diag(R_table_3rd))/sum(R_table_3rd)) # Returns 17.68%

### Accuracy of model
confusionMatrix(pred_P_7th, svm_test_justLabel)
confusionMatrix(pred_P_8th, svm_test_justLabel)
confusionMatrix(pred_P_9th, svm_test_justLabel)
#################### KNN Model ##############################

#load needed packages
library(tidyverse)
library(mlr)
library(class)
library(Biocomb)

# Model 1
knn_df <- df
knndrop <- c("name","category","deadline","launched","usd_pledged_real","gap")
knn_df <- knn_df[,!(names(knn_df) %in% knndrop)]
str(knn_df)


# KNN Create Test and Training Data Sets
# Create a 70/30 split using functions from caret
set.seed(101)
index = createDataPartition(knn_df$state, p = 0.7, list = F )
train1 = knn_df[index,]
test1 = knn_df[-index,]

summary(train1)
summary(test1)
dim(train1)
head(train1)
# Make sure you take the labels out of the testing data
knn_df_test1_noLabel<-test1[-c(2)]
(knn_df_test1_justLabel<-test1$state)
(head(knn_df_test1_noLabel))
str(knn_df_test1_justLabel)

knn_df_train1_noLabel<-train1[-c(2)]
(knn_df_train1_justLabel<-train1$state)
(head(knn_df_train1_noLabel))


#KNN Requires that ALL predictor variables be numeric
#Create dummy variables for country and main-category
train1$country <- as.numeric(train1$country)
train1$main_category <- as.numeric(train1$main_category)
str(train1)
test1$country <- as.numeric(test1$country)
test1$main_category <- as.numeric(test1$main_category)
str(test1)


#create color pallette
pal = c("lightseagreen","olivedrab3")

#Visualizations for the training data
ggplot(train1, aes(state,fill = state)) +
  geom_bar() +
  labs(x="Level", y="Count", fill="Success/Fail") +
  ggtitle("Sucess/Failure Distribution in Training Data Set 1") +
  theme(legend.position = "left")+
  scale_fill_manual(values=pal)

#Visualizations for the test data
ggplot(test1, aes(state,fill = state)) +
  geom_bar() +
  labs(x="Level", y="Count", fill="Success/Fail") +
  ggtitle("Success/Failure Distribution in Test Data Set 1") +
  theme(legend.position = "left")+
  scale_fill_manual(values=pal)

#Feature Selection using regression
options(scipen = 3)
trainreg <- train1
trainreg$state <- as.numeric(trainreg$state)
fit <- lm(state~., data=trainreg)
summary(fit) # show results
coefficients(fit) # model coefficients

# Chi squared test
trainchi <- train1
trainchi$state <- as.numeric(trainchi$state)
str(trainchi$state)
disc <- "equal interval width"
attrs.nominal=numeric()
chi_features <- select.inf.chi2(trainchi,disc.method=disc,attrs.nominal=attrs.nominal)
chi_features
str(chi_features)
chi_features$NumberFeature
chi_ordered <- chi_features[order(-chi_features$ChiSquare), ]
features_list <- (chi_ordered[1:20,1])
features_list

weights <- as.data.frame(gain.ratio(state~.,trainchi))
weights
str(weights)
features1<-rownames(weights)
weights$features <- features1
chi_weight <- weights[order(-weights[,1]), ]
chi_weight[1:20,]

# Create the kNN Model 1
# Setting up train controls
repeats = 3
numbers = 10
tunel = 10

set.seed(1234)
x <- trainControl(method = "repeatedcv",
                  number = numbers,
                  repeats = repeats,
                  classProbs = TRUE,
                  summaryFunction = twoClassSummary)

#Create the Model
model1 <- train(state~. , data = train1, method = "knn",
                preProcess = c("center","scale"),
                trControl = x,
                metric = "ROC",
                tuneLength = tunel)

# Summary of model
model1
plot(model1, main="kNN Number of Neighbors Probability Curve")

#create the predictions
# class predictions
knnPredict1 <- predict(model1,test1 )
knnPredict1
(cf_knn1 <-confusionMatrix(knnPredict1, knn_df_test1_justLabel ))


# probabilities
knnPredict1pb <- predict(model1,test1, type="prob" )
knnPredict1pb

library(ROCR)
pred_val1 <- prediction(knnPredict1[,2], knn_df_test1_justLabel)

perf_val1 <- performance(pred_val1,"auc")
perf_val1

# Plot AUC
perf_val1 <- performance(pred_val1, "tpr", "fpr")
plot(perf_val1, col = "green", lwd = 1.5)

#KS Stats
ks <- max(attr(perf_val1, "y.values")[[1]]-(attr(perf_val1, "x.values")[[1]]))
ks


#confusion Matrix
(KNN_table1<-table(knnPredict1, knn_df_test1_justLabel))
(KNN_error1 <- 1 - sum(diag(KNN_table1))/sum(KNN_table1))

KNN_df1 <- as.data.frame(KNN_table1)
plotK1 <- ggplot(KNN_df1)
plotK1 + geom_tile(aes(x=KNN_df1$knn_df_test1_justLabel, y=KNN_df1$knnPredict, fill=Freq)) + 
  scale_x_discrete(name="Actual Class") + scale_y_discrete(name="Predicted Class") + 
  scale_fill_gradientn(breaks=seq(from=0, to=65000, by=5500), colors = terrain.colors(10), guide="legend" ) + 
  labs(fill="Number\nPredicted", title="kNN Confusion Matrix Model 1")


# Model 2

#remove items with no backers. These are automatic failures. 51104 observations.
count((knn_df$backers < 1))
knn_df2 <- knn_df[-(which(knn_df$backers < 1)), ]
count((knn_df2$backers < 1))


# Create Test and Training Data Sets Model 2  
# Create a 70/30 split using functions from caret
set.seed(101)
index = createDataPartition(knn_df2$state, p = 0.7, list = F )
train2 = knn_df2[index,]
test2 = knn_df2[-index,]

summary(train2)
summary(test2)
dim(train2)
head(train2)
# Make sure you take the labels out of the testing data
knn_df_test2_noLabel<-test2[-c(2)]
(knn_df_test2_justLabel<-test2$state)
(head(knn_df_test2_noLabel))
str(knn_df_test2_justLabel)

knn_df_train2_noLabel<-train2[-c(2)]
(knn_df_train2_justLabel<-train2$state)
(head(knn_df_train2_noLabel))


# KNN Requires that ALL predictor variables be numeric
# Create dummy variables for country and main-category
train2$country <- as.numeric(train2$country)
train2$main_category <- as.numeric(train2$main_category)
str(train2)
test2$country <- as.numeric(test2$country)
test2$main_category <- as.numeric(test2$main_category)
str(test2)

# turn off scientific notation like 1e-09
options(scipen = 999) 
# create color pallette
pal = c("lightseagreen","olivedrab3")

# Visualizations for the training data
ggplot(train2, aes(state,fill = state)) +
  geom_bar() +
  labs(x="Level", y="Count", fill="Success/Fail") +
  ggtitle("Sucess/Failure Distribution in Training Data Set 2") +
  theme(legend.position = "left")+
  scale_fill_manual(values=pal)

# Visualizations for the test data
ggplot(test2, aes(state,fill = state)) +
  geom_bar() +
  labs(x="Level", y="Count", fill="Success/Fail") +
  ggtitle("Success/Failure Distribution in Test Data Set 2") +
  theme(legend.position = "left")+
  scale_fill_manual(values=pal)


# Setting up train controls for Model 2
repeats = 3
numbers = 10
tunel = 10

set.seed(1234)
x2 <- trainControl(method = "repeatedcv",
                   number = numbers,
                   repeats = repeats,
                   classProbs = TRUE,
                   summaryFunction = twoClassSummary)

# Create the Model 2
model2 <- train(state~. , data = train2, method = "knn",
                preProcess = c("center","scale"),
                trControl = x2,
                metric = "ROC",
                tuneLength = tunel)

# Summary of model 2
model2
plot(model2, main="kNN Number of Neighbors Probability Curve Model 2")

#create the predictions Model 2
# class predictions
knnPredict2 <- predict(model2,test2 )
knnPredict2
(cf_knn <-confusionMatrix(knnPredict2, knn_df_test2_justLabel ))


# probabilities Model 2
knnPredict2 <- predict(model2,test2, type="prob" )
knnPredict2

library(ROCR)
pred_val2 <- prediction(knnPredict2[,2], knn_df_test2_justLabel)

perf_val2 <- performance(pred_val2,"auc")
perf_val2

# Plot AUC
perf_val2 <- performance(pred_val2, "tpr", "fpr")
plot(perf_val2, col = "green", lwd = 1.5)

#KS Stats
ks2 <- max(attr(perf_val2, "y.values")[[1]]-(attr(perf_val2, "x.values")[[1]]))
ks2


#confusion Matrix
(KNN_table2<-table(knnPredict2, knn_df_test2_justLabel))
(KNN_error2 <- 1 - sum(diag(KNN_table2))/sum(KNN_table2))

KNN_df2 <- as.data.frame(KNN_table2)
plotK2 <- ggplot(KNN_df2)
plotK2 + geom_tile(aes(x=KNN_df2$knn_df_test2_justLabel, y=KNN_df2$knnPredict2, fill=Freq)) + 
  scale_x_discrete(name="Actual Class") + scale_y_discrete(name="Predicted Class") + 
  scale_fill_gradientn(breaks=seq(from=0, to=65000, by=5500), colors = terrain.colors(10), guide="legend" ) + 
  labs(fill="Number\nPredicted", title="kNN Confusion Matrix Model 2")



