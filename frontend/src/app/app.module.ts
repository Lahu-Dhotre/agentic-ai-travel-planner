import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { CommonModule } from '@angular/common';

import { AppComponent } from './app.component';
import { TripPlannerComponent } from './trip-planner/trip-planner.component';
import { TripPlannerService } from './services/trip-planner.service';

@NgModule({
  declarations: [
    AppComponent,
    TripPlannerComponent
  ],
  imports: [
    BrowserModule,
    CommonModule,
    ReactiveFormsModule,
    HttpClientModule
  ],
  providers: [
    TripPlannerService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
