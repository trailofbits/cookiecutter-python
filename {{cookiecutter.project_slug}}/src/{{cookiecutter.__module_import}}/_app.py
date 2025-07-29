"""FastAPI application setup."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from {{ cookiecutter.__project_import }} import __version__

app = FastAPI(
    title="{{ cookiecutter.project_name }}",
    description="{{ cookiecutter.project_description }}",
    version=__version__,
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root() -> dict[str, str]:
    """Root endpoint."""
    return {"message": "{{ cookiecutter.project_name }} API", "version": __version__}


@app.get("/health")
async def health() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "ok"}