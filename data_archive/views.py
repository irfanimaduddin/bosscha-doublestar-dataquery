from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views.generic import DetailView, TemplateView

from .models import *

import csv
import datetime as dt
import numpy as np
import pandas as pd

from plotly.offline import plot 
import plotly.graph_objs as go


class HomeView(TemplateView):
    """ A class for Home View"""
    template_name="home.html"

    model = MainView

    # paginate_by = 10

    queryset=MainView.objects.all()

    def get(self, request, *args, **kwargs):
        context={"queryset": self.queryset}
        return render(request, self.template_name, context)

    def export_csv(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=bzds' + str(dt.now())+'.csv'

        writer = csv.writer(response, delimiter=';')
        writer.writerow("Bosscha/Zeiss Double Star Archive\n")
        writer.writerow("Download time = %s" %(dt.now()))
        writer.writerow("Contact = irfanimadudin[at]gmail[dot]com")

        writer.writerow([
            'jasname',
            'discoverer',
            'ra',
            'dec',
            'GmagA',
            'GmagB',
            'gaiasep',
            'gaiaPA',
            'probability',
            'category'
        ])

        for query in self.queryset:
            writer.writerow([
                query.jasname,
                query.discoverer,
                query.ra,
                query.decl,
                query.gmaga,
                query.gmagb,
                query.gaia_sep,
                query.gaia_pa,
                query.probability,
                query.cat                
            ])
        
        return response

class DoubleStarObjMixin(object):
    # A class for getting object    
    model = MainView
    
    def get_object(self):
        discoverer = self.kwargs.get("discoverer")
        instance = None
        if discoverer is not None:
            instance = get_object_or_404(self.model, discoverer=discoverer)
        return instance

class ObjectView(DoubleStarObjMixin, DetailView):
    # A class for Object Detail View
    template_name = "objectpage.html"

    list_field = (
        'jasname',
        'discoverer',
        'ads',
        'bds',
        'ids',
        'wds',
        'ra',
        'decl',
        'gmaga',
        'gmagb',
        'gaia_sep',
        'gaia_pa',
        'probability',
        'cat',
        'epoch',
        'data_pa',
        'data_sep',
        'count',
        'observer_sign',
        'pub_sign',
        'method_sign'
    )

    def get(self, request, discoverer=None, *args, **kwargs):
        # GET Method
        instance = self.get_object()

        if instance is not None:
            observed = PageView.objects.filter(discoverer=discoverer)
            data = observed.values()
            for i in range(len(data)):
                if data[i]['epoch'] is None:
                    data[i]['epoch'] = ''

            keyval = observed.values(
                'jasname',
                'discoverer',
                'ads',
                'bds',
                'ids',
                'wds',
                'ra',
                'decl',
                'gmaga',
                'gmagb',
                'gaia_sep',
                'gaia_pa',
                'probability',
                'cat'
                )[0]

            if keyval['ads'] is None:
                keyval['ads'] = ''
            if keyval['bds'] is None:
                keyval['bds'] = ''
            if keyval['ids'] is None:
                keyval['ids'] = ''
            if keyval['wds'] is None:
                keyval['wds'] = ''
            if keyval['ra'] is None:
                keyval['ra'] = ''
            if keyval['decl'] is None:
                keyval['decl'] = ''
            if keyval['gmaga'] is None:
                keyval['gmaga'] = ''
            if keyval['gmagb'] is None:
                keyval['gmagb'] = ''
            if keyval['gaia_sep'] is None:
                keyval['gaia_sep'] = ''
            if keyval['gaia_pa'] is None:
                keyval['gaia_pa'] = ''
            if keyval['probability'] is None:
                keyval['probability'] = ''
            if keyval['cat'] is None:
                keyval['cat'] = ''

        data_value = data.values_list('epoch', 'data_pa', 'data_sep')
        df = pd.DataFrame(data_value, columns=['epoch', 'tetha', 'rho'])

        if df['tetha'].isna().any() == True:
            df = df[~df['tetha'].isna()].reset_index(drop=True)
        if df['rho'].isna().any() == True:
            df = df[~df['rho'].isna()].reset_index(drop=True)

        df['epoch'].fillna(value='', inplace=True)
        df['tetha'] = df['tetha'].astype(float)
        df['rho'] = df['rho'].astype(float)

        def graph_func(df):
            # Converting polar to cartesian coordinates
            x = df["rho"].values * np.cos(np.deg2rad(df["tetha"].values))
            y = df["rho"].values * np.sin(np.deg2rad(df["tetha"].values))

            fig = go.Figure()
            fig.add_trace(go.Scatter(x=x, y=y, mode='markers'))
            fig.update_traces(
                customdata  = np.stack((df['epoch'], df['rho'], df['tetha']), axis=-1),
                hovertemplate = 'Epoch: %{customdata[0]} <br>Rho: %{customdata[1]}"<br>Tetha: %{customdata[2]} deg<extra></extra>',
                marker=dict(size=5, color='black')
            )    
            fig.update_layout(
                plot_bgcolor="#fff",
                width=500,
                height=500,
                dragmode='pan',
                xaxis=dict(
                    zerolinecolor="#808080",  # X-axis line color 
                    showgrid=True, # X-axis grid lines
                    gridcolor="#E1E1E1", # Grid line color
                    rangemode='tozero', # Stretch plot to zero value
                    showline=True, 
                    autorange=True,
                    nticks=0,

                ),
                yaxis=dict(
                    zerolinecolor="#808080",  # Y-axis line color
                    showgrid=True, # Y-axis grid lines
                    gridcolor="#E1E1E1", # Grid line color
                    rangemode='tozero', # Stretch plot to zero value
                    showline=True, 
                    autorange=True,
                    nticks=0,
                )
            ) 

            config = {
                'displaylogo': False,
                'responsive': True,
                'scrollZoom': True,
                'modeBarButtonsToRemove': ['zoom2d','pan','select2d','lasso2d','zoomIn2d','zoomOut2d','autoScale2d'],
                'toImageButtonOptions': {
                    'format': 'png', # one of png, svg, jpeg, webp
                    'filename': '%s_orbitalplot'%(discoverer),
                    'height': 600,
                    'width': 600,
                    'scale': 1 # Multiply title/legend/axis/canvas sizes by this factor
            }
            }

            plot_div = plot(fig, output_type='div', config=config)

            return plot_div

        context = {
            'observed': observed,
            'keyval': keyval,
            'plot': graph_func(df)
            }

        return render(request=request, 
        template_name=self.template_name,
        context=context)