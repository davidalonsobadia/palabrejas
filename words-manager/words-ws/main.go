package main

import (
  "gorm.io/driver/postgres"
  "gorm.io/gorm"
  "log"
  "net/http"
  "github.com/gorilla/mux"
  "encoding/json"
)

type Word struct {
    Id string
    Word string
    Ascii_word string
    Definition string
}

func allWords(w http.ResponseWriter, r *http.Request) {

    dsn := "host=127.0.0.1 user=postgres password=postgres dbname=postgres port=5432"
    db, err := gorm.Open(postgres.Open(dsn), &gorm.Config{})
    if err != nil {
        panic("Failed to connect to the database")
    }

    var words []Word
    db.Find(&words)

    json.NewEncoder(w).Encode(words)
}

func getSpecificWords(w http.ResponseWriter, r *http.Request) {
    // Continue here
     dsn := "host=127.0.0.1 user=postgres password=postgres dbname=postgres port=5432"
     db, err := gorm.Open(postgres.Open(dsn), &gorm.Config{})
     if err != nil {
         panic("Failed to connect to the database")
     }

     var words []Word
     db.Find(&words)

     var results []string
     for i, word range words {
        if len(word) < 3 {
            continue
        }
        if
     }
}

func handleRequests() {
    myRouter := mux.NewRouter().StrictSlash(true)
    myRouter.HandleFunc("/words", allWords).Methods("GET")
    log.Fatal(http.ListenAndServe(":8080", myRouter))
}

func main() {

    handleRequests()
}


