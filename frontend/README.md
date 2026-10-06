# Agentic Trip Planner - Frontend

A modern Angular application for planning trips using AI-powered agents. This frontend communicates with a FastAPI backend that orchestrates multiple AI agents to create detailed travel plans.

## 🚀 Features

- **Reactive Forms**: Clean, validated form inputs with real-time error messages
- **Modern UI**: Beautiful gradient design with smooth animations
- **Responsive**: Works seamlessly on desktop, tablet, and mobile devices
- **Type-Safe**: Full TypeScript support with strict typing
- **Error Handling**: Comprehensive error handling and user feedback
- **Date Validation**: Ensures end date is after start date
- **Optional Budget**: Budget field is optional for flexible trip planning

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- **Node.js** (v18 or higher)
- **npm** (v9 or higher)
- **Angular CLI** (optional, but recommended)

## 🛠️ Installation

1. **Navigate to the frontend directory**:
   ```powershell
   cd frontend
   ```

2. **Install dependencies**:
   ```powershell
   npm install
   ```

3. **Install Angular CLI globally** (if not already installed):
   ```powershell
   npm install -g @angular/cli
   ```

## 🏃‍♂️ Running the Application

1. **Start the development server**:
   ```powershell
   npm start
   ```
   
   Or using Angular CLI:
   ```powershell
   ng serve
   ```

2. **Open your browser** and navigate to:
   ```
   http://localhost:4200
   ```

3. **Make sure the backend is running** on `http://localhost:8000` for the app to function properly.

## 📁 Project Structure

```
frontend/
├── src/
│   ├── app/
│   │   ├── models/
│   │   │   ├── trip-request.model.ts      # TripRequest interface
│   │   │   └── trip-response.model.ts     # TripResponse interface
│   │   ├── services/
│   │   │   └── trip-planner.service.ts    # HTTP service for API calls
│   │   ├── trip-planner/
│   │   │   ├── trip-planner.component.ts   # Component logic
│   │   │   ├── trip-planner.component.html # Component template
│   │   │   └── trip-planner.component.css  # Component styles
│   │   ├── app.component.ts               # Root component
│   │   └── app.module.ts                  # App module configuration
│   ├── environments/
│   │   ├── environment.ts                 # Development environment
│   │   └── environment.prod.ts            # Production environment
│   ├── index.html                         # Main HTML file
│   ├── main.ts                            # Bootstrap entry point
│   └── styles.css                         # Global styles
├── angular.json                           # Angular configuration
├── package.json                           # Dependencies
├── tsconfig.json                          # TypeScript configuration
└── README.md                              # This file
```

## 🎨 Components

### TripPlannerComponent

The main component that handles:
- Trip planning form with reactive validation
- Communication with the backend API
- Display of generated trip plans
- Error handling and loading states

**Form Fields:**
- **Destination** (required): Where you want to travel
- **Start Date** (required): Trip start date
- **End Date** (required): Trip end date (must be after start date)
- **Budget** (optional): Budget in USD

### TripPlannerService

HTTP service that:
- Sends POST requests to `/plan-trip` endpoint
- Handles API responses and errors
- Provides typed interfaces for requests/responses

## 🔧 Configuration

### Backend API URL

Update the API URL in `src/app/services/trip-planner.service.ts`:

```typescript
private apiUrl = 'http://localhost:8000'; // Change this to your backend URL
```

Or use environment variables in `src/environments/environment.ts`:

```typescript
export const environment = {
  production: false,
  apiUrl: 'http://localhost:8000'
};
```

## 🎯 API Integration

The frontend expects the backend to have the following endpoint:

**POST** `/plan-trip`

**Request Body:**
```json
{
  "destination": "Paris",
  "start_date": "2025-06-01",
  "end_date": "2025-06-07",
  "budget": 3000
}
```

**Response:**
```json
{
  "plan": "Detailed trip plan text..."
}
```

## 🧪 Building for Production

To create a production build:

```powershell
npm run build
```

Or:

```powershell
ng build --configuration production
```

The build artifacts will be stored in the `dist/` directory.

## 🎨 Customization

### Styling

- **Global styles**: Edit `src/styles.css`
- **Component styles**: Edit `src/app/trip-planner/trip-planner.component.css`
- **Color scheme**: Update gradient colors in CSS files

### Validation Rules

Modify validation in `src/app/trip-planner/trip-planner.component.ts`:

```typescript
this.tripForm = this.fb.group({
  destination: ['', [Validators.required, Validators.minLength(2)]],
  start_date: ['', [Validators.required]],
  end_date: ['', [Validators.required]],
  budget: [null, [Validators.min(0)]]
});
```

## 🐛 Troubleshooting

### CORS Issues

If you encounter CORS errors, ensure your FastAPI backend has CORS enabled:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Port Already in Use

If port 4200 is already in use, run on a different port:

```powershell
ng serve --port 4300
```

## 📦 Technologies Used

- **Angular 17**: Frontend framework
- **TypeScript**: Type-safe programming
- **Reactive Forms**: Form handling and validation
- **HttpClient**: HTTP communication
- **RxJS**: Reactive programming with observables
- **CSS3**: Modern styling with animations

## 🤝 Integration with Backend

This frontend is designed to work with:
- **Backend**: Python FastAPI
- **LLM Orchestration**: Microsoft Autogen
- **API Endpoint**: `/plan-trip`

Ensure the backend is running before starting the frontend application.

## 📝 License

This project is part of the Agentic AI Travel Planner full-stack application.

## 👨‍💻 Development

For development:
1. The app will automatically reload if you change any source files
2. Use Chrome DevTools for debugging
3. Check browser console for errors
4. Use Angular DevTools extension for component inspection

---

**Happy Trip Planning! ✈️🌍**
