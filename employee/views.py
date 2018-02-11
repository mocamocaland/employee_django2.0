from django.views import generic
from .form import SearchForm
from .models import Employee


class IndexView(generic.ListView):
    model = Employee

    def get_context_data(self):
        """テンプレートへ渡す辞書の作成"""
        form = SearchForm(self.request.GET) # 元の辞書にformを追加 カッコ内に何もなくても問題なし
        return context

    def get_queryset(self):
        """テンプレートへ渡す「employee_list」を作成する"""
        form = SearchForm(self.request.GET)
        form.is_valid() # これをしないと、cleaned_dataができない！！

        # まず、全社員を取得
        queryset = super().get_queryset()

        # 部署の選択があれば、部署で絞り込み(filter)
        department = form.cleaned_data['department']
        if department:
            queryset = queryset.filter(department=department)

        # サークルの選択があれば、サークルで絞り込み(filter)
        club = form.cleaned_data['club']
        if club:
            queryset = queryset.filter(club=club)
        return queryset