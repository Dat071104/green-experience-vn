from flask import Blueprint, render_template, request, abort
from data.static_data import (
    DESTINATIONS, DESTINATIONS_BY_ID, 
    TOURS_BY_DESTINATION, TOURS_BY_ID,
    HOMESTAYS, COMMUNITY_ACTIVITIES, PLASTIC_FREE_SPOTS
)

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    featured_destinations = DESTINATIONS[:3]
    return render_template('home.html', destinations=featured_destinations)

@main_bp.route('/destinations')
def destinations():
    region = request.args.get('region', 'all')
    if region == 'all':
        filtered = DESTINATIONS
    else:
        filtered = [d for d in DESTINATIONS if d.get('region') == region]
    regions = sorted(set(d['region'] for d in DESTINATIONS))
    return render_template('destinations.html',
                           destinations=filtered,
                           current_region=region,
                           regions=regions)

@main_bp.route('/destinations/<dest_id>')
def destination_detail(dest_id):
    dest = DESTINATIONS_BY_ID.get(dest_id)
    if not dest:
        abort(404)
    tours = TOURS_BY_DESTINATION.get(dest_id, [])
    homestays = [h for h in HOMESTAYS if h.get('destinationId') == dest_id]
    activities = [a for a in COMMUNITY_ACTIVITIES if a.get('destinationId') == dest_id]
    spots = [s for s in PLASTIC_FREE_SPOTS if s.get('destinationId') == dest_id]
    return render_template('destination_detail.html', dest=dest, tours=tours,
                           homestays=homestays, activities=activities, spots=spots)

@main_bp.route('/tours/<tour_id>')
def tour_detail(tour_id):
    tour = TOURS_BY_ID.get(tour_id)
    if not tour:
        abort(404)
    dest = DESTINATIONS_BY_ID.get(tour.get('destinationId'))
    return render_template('tour_detail.html', tour=tour, dest=dest)

@main_bp.route('/homestays')
def homestays_page():
    return render_template('homestays.html', homestays=HOMESTAYS)

@main_bp.route('/community')
def community_page():
    return render_template('community.html', activities=COMMUNITY_ACTIVITIES)

@main_bp.route('/co2-calculator')
def co2_calculator():
    return render_template('co2_calculator.html')

@main_bp.route('/about')
def about():
    return render_template('about.html')
