package main

import (
	"github.com/go-chi/chi/v5"
	"log"
	"net/http"
)

type Handler struct {
	*chi.Mux
}

type Response struct {
    point Point `json: point`
}

type Point struct{
    x: int `json:x`
    y: int `json:y`
    direction: string `json:direction`
}

func main() {
	h := &Handler{
		Mux: chi.NewMux(),
	}

	h.Post("/command", func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusCreated)
		_, err := w.Write([]byte(`{"point"}`))
		if err != nil {
			log.Printf("Error: %v", err)
		}
	})

	log.Fatal(
		http.ListenAndServe(":3001", h),
	)
}
