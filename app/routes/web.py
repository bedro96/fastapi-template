"""Web UI Routes with Jinja2 Templates"""

from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.order import Order
from typing import Optional

router = APIRouter(tags=["web"])
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    """Display all orders"""
    orders = db.query(Order).all()
    return templates.TemplateResponse(
        "index.html", {"request": request, "orders": orders}
    )


@router.get("/orders/new", response_class=HTMLResponse)
def new_order_form(request: Request):
    """Display form to create new order"""
    return templates.TemplateResponse("order_form.html", {"request": request})


@router.post("/orders/new")
def create_order_form(
    name: str = Form(...),
    quantity: int = Form(...),
    description: Optional[str] = Form(None),
    db: Session = Depends(get_db),
):
    """Create new order from form submission"""
    order = Order(name=name, quantity=quantity, description=description)
    db.add(order)
    db.commit()
    return RedirectResponse(url="/", status_code=303)


@router.get("/orders/{order_id}/edit", response_class=HTMLResponse)
def edit_order_form(request: Request, order_id: int, db: Session = Depends(get_db)):
    """Display form to edit existing order"""
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        return RedirectResponse(url="/", status_code=303)
    return templates.TemplateResponse(
        "order_form.html", {"request": request, "order": order}
    )


@router.post("/orders/{order_id}/edit")
def update_order_form(
    order_id: int,
    name: str = Form(...),
    quantity: int = Form(...),
    description: Optional[str] = Form(None),
    db: Session = Depends(get_db),
):
    """Update order from form submission"""
    order = db.query(Order).filter(Order.id == order_id).first()
    if order:
        order.name = name  # type: ignore[assignment]
        order.quantity = quantity  # type: ignore[assignment]
        order.description = description  # type: ignore[assignment]
        db.commit()
    return RedirectResponse(url="/", status_code=303)


@router.post("/orders/{order_id}/delete")
def delete_order_form(order_id: int, db: Session = Depends(get_db)):
    """Delete order"""
    order = db.query(Order).filter(Order.id == order_id).first()
    if order:
        db.delete(order)
        db.commit()
    return RedirectResponse(url="/", status_code=303)
