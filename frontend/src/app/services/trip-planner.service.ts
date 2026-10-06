import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { TripRequest } from '../models/trip-request.model';
import { TripResponse } from '../models/trip-response.model';

@Injectable({
  providedIn: 'root'
})
export class TripPlannerService {
  private apiUrl = 'http://localhost:8000'; // FastAPI backend URL

  constructor(private http: HttpClient) {}

  /**
   * Send trip planning request to FastAPI backend
   * @param tripRequest - The trip details
   * @returns Observable with the trip plan
   */
  planTrip(tripRequest: TripRequest): Observable<TripResponse> {
    return this.http.post<TripResponse>(`${this.apiUrl}/trips/plan`, tripRequest)
      .pipe(
        catchError(this.handleError)
      );
  }

  /**
   * Handle HTTP errors
   * @param error - The HTTP error response
   * @returns Observable that errors with a user-friendly message
   */
  private handleError(error: HttpErrorResponse): Observable<never> {
    let errorMessage = 'An error occurred while planning your trip.';
    
    if (error.error instanceof ErrorEvent) {
      // Client-side or network error
      errorMessage = `Error: ${error.error.message}`;
    } else {
      // Backend error
      errorMessage = `Server Error: ${error.status} - ${error.message}`;
      if (error.error && error.error.detail) {
        errorMessage = error.error.detail;
      }
    }
    
    console.error('Trip planning error:', error);
    return throwError(() => new Error(errorMessage));
  }
}
