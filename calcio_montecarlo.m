% Creazione di una figura
close all
figure;
hold on;
axis equal;

% Definizione delle dimensioni del rettangolo
width = 5;
height = 3;

% Definizione delle posizioni dei vertici del rettangolo
xRect = [0 width width 0 0];
yRect = [0 0 height height 0];

% Disegno del rettangolo
fill(xRect, yRect, 'b');

% Definizione del raggio delle circonferenze
r = 0.5;

% Posizioni dei centri delle circonferenze
centers = [1 0.75; 4 0.75; 1 2.25; 4 2.25];

% Disegno delle circonferenze
theta = linspace(0, 2*pi, 100); % Angoli per il cerchio
for i = 1:size(centers, 1)
    xCircle = r * cos(theta) + centers(i, 1);
    yCircle = r * sin(theta) + centers(i, 2);
    fill(xCircle, yCircle, 'w'); % Riempie l'interno delle circonferenze di bianco
    plot(xCircle, yCircle, 'r'); % Disegna il bordo delle circonferenze in rosso
end

% Impostazioni degli assi
xlim([-1, width + 1]);
ylim([-1, height + 1]);

% Titolo e etichette degli assi
title('Porta');
xlabel('Asse X');
ylabel('Asse Y');

hold off;

%live goal
a=0;
b=width;
c=0;
d=height;
for i=1:10
pause
x_rand_live = a + (b-a).*rand(1);
y_rand_live= c + (d-c).*rand(1);

hold on
plot(x_rand_live,y_rand_live,'ok','LineWidth',15)
end

%monte carlo goasl
attempts=1000;
x_rand = a + (b-a).*rand(attempts,1);
y_rand= c + (d-c).*rand(attempts,1);

hold on
plot(x_rand,y_rand,'ok','LineWidth',10)


%theoretical probability

Area_rect=width*height;
Area_1_circle=pi*r^2;
Goal_prob=4*Area_1_circle/Area_rect

%statistical probability
goal=zeros(attempts,1);
for i=1:attempts
    point=[x_rand(i),y_rand(i)];
    if (norm(point-centers(1,:)) <= r) || ...
            (norm(point-centers(2,:)) <= r) || ...
            norm(point-centers(3,:)) <= r || ...
            (norm(point-centers(4,:))) <= r
        goal(i)=1;
    else
        goal(i)=0;
    end
end
Stat_prob=sum(goal)/attempts