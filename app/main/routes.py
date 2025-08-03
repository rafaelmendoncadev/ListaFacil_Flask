from flask import render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required, current_user
from app import db
from app.main import bp
from app.models import User, List, Item, Category, PurchaseHistory
from app.forms import ListForm, ItemForm, CategoryForm

@bp.route('/')
def index():
    return render_template('index.html', title='ListaFácil')

@bp.route('/dashboard')
@login_required
def dashboard():
    lists = current_user.lists.filter_by(archived=False).order_by(List.created_at.desc()).all()
    archived_lists = current_user.lists.filter_by(archived=True).count()
    total_items = db.session.query(Item).join(List).filter(List.user_id == current_user.id).count()
    return render_template('dashboard.html', title='Painel', lists=lists, 
                         archived_lists=archived_lists, total_items=total_items)

@bp.route('/create_list', methods=['GET', 'POST'])
@login_required
def create_list():
    form = ListForm()
    if form.validate_on_submit():
        shopping_list = List(
            name=form.name.data,
            description=form.description.data,
            category=form.category.data,
            user_id=current_user.id
        )
        db.session.add(shopping_list)
        db.session.commit()
        flash('Lista criada com sucesso!', 'success')
        return redirect(url_for('main.list_detail', id=shopping_list.id))
    return render_template('create_list.html', title='Criar Lista', form=form)

@bp.route('/list/<int:id>')
@login_required
def list_detail(id):
    shopping_list = List.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    items = shopping_list.items.order_by(Item.position, Item.created_at).all()
    categories = Category.query.all()
    form = ItemForm()
    form.category_id.choices = [(0, 'Sem Categoria')] + [(c.id, c.name) for c in categories]
    return render_template('list_detail.html', title=shopping_list.name, 
                         shopping_list=shopping_list, items=items, form=form, list=shopping_list, categories=categories)

@bp.route('/add_item/<int:list_id>', methods=['POST'])
@login_required
def add_item(list_id):
    shopping_list = List.query.filter_by(id=list_id, user_id=current_user.id).first_or_404()
    form = ItemForm()
    categories = Category.query.all()
    form.category_id.choices = [(0, 'Sem Categoria')] + [(c.id, c.name) for c in categories]
    
    if form.validate_on_submit():
        item = Item(
            name=form.name.data,
            category_id=form.category_id.data if form.category_id.data != 0 else None,
            quantity=form.quantity.data or 1,
            unit=form.unit.data,
            estimated_price=form.estimated_price.data,
            notes=form.notes.data,
            list_id=list_id,
            position=shopping_list.items.count()
        )
        db.session.add(item)
        db.session.commit()
        flash('Item adicionado com sucesso!', 'success')
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'{field}: {error}', 'error')
    
    return redirect(url_for('main.list_detail', id=list_id))

@bp.route('/toggle_item/<int:item_id>', methods=['POST'])
@login_required
def toggle_item(item_id):
    item = Item.query.join(List).filter(
        Item.id == item_id,
        List.user_id == current_user.id
    ).first_or_404()
    
    item.is_purchased = not item.is_purchased
    
    if item.is_purchased:
        # Add to purchase history
        history = PurchaseHistory(
            user_id=current_user.id,
            item_name=item.name,
            category=item.item_category.name if item.item_category else None,
            price=item.estimated_price
        )
        db.session.add(history)
    
    db.session.commit()
    return jsonify({'success': True, 'is_purchased': item.is_purchased})

@bp.route('/delete_item/<int:item_id>', methods=['POST'])
@login_required
def delete_item(item_id):
    print(f"DEBUG: Tentando excluir item {item_id}")
    print(f"DEBUG: Método: {request.method}")
    print(f"DEBUG: Form data: {request.form}")
    
    try:
        item = Item.query.join(List).filter(
            Item.id == item_id,
            List.user_id == current_user.id
        ).first_or_404()
        
        print(f"DEBUG: Item encontrado: {item.name}")
        
        list_id = item.list_id
        db.session.delete(item)
        db.session.commit()
        
        print(f"DEBUG: Item excluído com sucesso")
        
        flash('Item excluído com sucesso!', 'success')
        return redirect(url_for('main.list_detail', id=list_id))
        
    except Exception as e:
        print(f"DEBUG: Erro ao excluir item: {str(e)}")
        db.session.rollback()
        flash('Erro ao excluir item', 'error')
        return redirect(url_for('main.dashboard'))

@bp.route('/edit_item', methods=['POST'])
@login_required
def edit_item():
    print(f"DEBUG: Editando item")
    print(f"DEBUG: Form data: {request.form}")
    
    try:
        item_id = request.form.get('item_id')
        list_id = request.form.get('list_id')
        
        # Verifica se o item pertence ao usuário
        item = Item.query.join(List).filter(
            Item.id == item_id,
            List.user_id == current_user.id
        ).first_or_404()
        
        print(f"DEBUG: Item encontrado: {item.name}")
        
        # Atualiza os dados do item
        item.name = request.form.get('name')
        item.quantity = float(request.form.get('quantity')) if request.form.get('quantity') else None
        item.unit = request.form.get('unit')
        item.estimated_price = float(request.form.get('estimated_price')) if request.form.get('estimated_price') else None
        item.notes = request.form.get('notes')
        
        # Atualiza categoria se fornecida
        category_id = request.form.get('category_id')
        if category_id:
            category = Category.query.filter_by(id=category_id).first()
            item.item_category = category
        else:
            item.item_category = None
        
        db.session.commit()
        
        print(f"DEBUG: Item editado com sucesso")
        
        flash('Item editado com sucesso!', 'success')
        return redirect(url_for('main.list_detail', id=list_id))
        
    except Exception as e:
        print(f"DEBUG: Erro ao editar item: {str(e)}")
        db.session.rollback()
        flash('Erro ao editar item', 'error')
        return redirect(url_for('main.dashboard'))

@bp.route('/archive_list/<int:list_id>', methods=['POST'])
@login_required
def archive_list(list_id):
    shopping_list = List.query.filter_by(id=list_id, user_id=current_user.id).first_or_404()
    shopping_list.archived = not shopping_list.archived
    db.session.commit()
    
    action = 'arquivada' if shopping_list.archived else 'desarquivada'
    flash(f'Lista {action} com sucesso!', 'success')
    return redirect(url_for('main.dashboard'))

@bp.route('/delete_list/<int:list_id>', methods=['POST'])
@login_required
def delete_list(list_id):
    shopping_list = List.query.filter_by(id=list_id, user_id=current_user.id).first_or_404()
    db.session.delete(shopping_list)
    db.session.commit()
    flash('Lista excluída com sucesso!', 'success')
    return redirect(url_for('main.dashboard'))

@bp.route('/categories')
@login_required
def categories():
    categories = Category.query.all()
    form = CategoryForm()
    return render_template('categories.html', title='Categorias', categories=categories, form=form)

@bp.route('/add_category', methods=['POST'])
@login_required
def add_category():
    form = CategoryForm()
    if form.validate_on_submit():
        category = Category(
            name=form.name.data,
            color=form.color.data or '#6B7280'
        )
        db.session.add(category)
        db.session.commit()
        flash('Categoria adicionada com sucesso!', 'success')
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'{field}: {error}', 'error')
    
    return redirect(url_for('main.categories'))

@bp.route('/update_item_positions', methods=['POST'])
@login_required
def update_item_positions():
    data = request.get_json()
    positions = data.get('positions', [])
    
    for pos_data in positions:
        item = Item.query.join(List).filter(
            Item.id == pos_data['id'],
            List.user_id == current_user.id
        ).first()
        if item:
            item.position = pos_data['position']
    
    db.session.commit()
    return jsonify({'success': True})

@bp.route('/purchase_history')
@login_required
def purchase_history():
    history = current_user.purchase_history.order_by(PurchaseHistory.purchased_at.desc()).limit(50).all()
    return render_template('purchase_history.html', title='Histórico de Compras', history=history)