import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { TripPlannerService } from '../services/trip-planner.service';
import { TripRequest } from '../models/trip-request.model';

@Component({
  selector: 'app-trip-planner',
  templateUrl: './trip-planner.component.html',
  styleUrls: ['./trip-planner.component.css']
})
export class TripPlannerComponent implements OnInit {
  tripForm!: FormGroup;
  tripPlan: string[] = [];
  isLoading = false;
  errorMessage: string | null = null;

  constructor(
    private fb: FormBuilder,
    private tripPlannerService: TripPlannerService
  ) {}

  ngOnInit(): void {
    this.initializeForm();
  }

  /**
   * Initialize the reactive form with validation
   */
  private initializeForm(): void {
    const today = new Date().toISOString().split('T')[0];
    
    this.tripForm = this.fb.group({
      destination: ['', [Validators.required, Validators.minLength(2)]],
      start_date: ['', [Validators.required]],
      end_date: ['', [Validators.required]],
      budget: [null, [Validators.min(0)]]
    }, {
      validators: this.dateRangeValidator
    });
  }

  /**
   * Custom validator to ensure end_date is after start_date
   */
  private dateRangeValidator(group: FormGroup): { [key: string]: boolean } | null {
    const startDate = group.get('start_date')?.value;
    const endDate = group.get('end_date')?.value;
    
    if (startDate && endDate && new Date(endDate) <= new Date(startDate)) {
      return { invalidDateRange: true };
    }
    
    return null;
  }

  /**
   * Handle form submission
   */
  onSubmit(): void {
    if (this.tripForm.valid) {
      this.isLoading = true;
      this.errorMessage = null;
    this.tripPlan = [];

      const tripRequest: TripRequest = {
        destination: this.tripForm.value.destination,
        start_date: this.tripForm.value.start_date,
        end_date: this.tripForm.value.end_date,
        budget: this.tripForm.value.budget || null
      };

      this.tripPlannerService.planTrip(tripRequest).subscribe({
        next: (response) => {
          this.tripPlan = response.itinerary;
          this.isLoading = false;
        },
        error: (error) => {
          this.errorMessage = error.message || 'Failed to generate trip plan. Please try again.';
          this.isLoading = false;
        }
      });
    } else {
      // Mark all fields as touched to show validation errors
      Object.keys(this.tripForm.controls).forEach(key => {
        this.tripForm.get(key)?.markAsTouched();
      });
    }
  }

  /**
   * Reset the form and clear results
   */
  onReset(): void {
    this.tripForm.reset();
  this.tripPlan = [];
    this.errorMessage = null;
  }

  /**
   * Get error message for a form field
   */
  getFieldError(fieldName: string): string | null {
    const field = this.tripForm.get(fieldName);
    
    if (field?.hasError('required') && field.touched) {
      return `${this.getFieldLabel(fieldName)} is required`;
    }
    
    if (field?.hasError('minLength') && field.touched) {
      return `${this.getFieldLabel(fieldName)} must be at least 2 characters`;
    }
    
    if (field?.hasError('min') && field.touched) {
      return 'Budget must be a positive number';
    }
    
    return null;
  }

  /**
   * Get human-readable field label
   */
  private getFieldLabel(fieldName: string): string {
    const labels: { [key: string]: string } = {
      destination: 'Destination',
      start_date: 'Start Date',
      end_date: 'End Date',
      budget: 'Budget'
    };
    return labels[fieldName] || fieldName;
  }

  /**
   * Check if date range is invalid
   */
  get hasInvalidDateRange(): boolean {
    return this.tripForm.hasError('invalidDateRange') && 
           this.tripForm.get('start_date')?.touched === true &&
           this.tripForm.get('end_date')?.touched === true;
  }
}
