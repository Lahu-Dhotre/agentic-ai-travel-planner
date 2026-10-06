export interface TripRequest {
  destination: string;
  start_date: string; // 'YYYY-MM-DD'
  end_date: string;   // 'YYYY-MM-DD'
  budget?: number | null;
}
